import nltk
nltk.download('punkt')

def tokenize_script(script_text: str, language: str) -> list[str]:
    try:
        sentences = nltk.sent_tokenize(script_text, language=language.lower())
        sentences = [s.strip() for s in sentences if s.strip()]
        return sentences
    except LookupError:
        print(f"Error: NLTK tokenizer for language '{language}' not found or downloaded.")
        return [s.strip() for s in script_text.replace('\n', ' ').split('.') if s.strip()]
    except Exception as e:
        print(f"An unexpected error occurred during tokenization: {e}")
        return [s.strip() for s in script_text.replace('\n', ' ').split('.') if s.strip()]


WPM_PACE = { "slow": 100, "medium": 140, "fast": 180}
DEFAULT_INTER_SENTENCE_SILENCE = 0.5

def calculate_timed_sentences(sentences: list[str], pace_type: str, inter_sentence_silence_seconds: float = DEFAULT_INTER_SENTENCE_SILENCE) -> tuple[list[tuple[float, float, str]], float]:
    wpm = WPM_PACE.get(pace_type.lower(), WPM_PACE["medium"])
    timed_sentences_with_ends = []
    cumulative_time_seconds = 0.0
    for i, sentence in enumerate(sentences):
        current_sentence_start_time = cumulative_time_seconds
        words = [word for word in sentence.split() if word] 
        word_count = len(words)
        estimated_speech_duration_seconds = (word_count / wpm) * 60 if wpm > 0 else 0
        current_sentence_end_time = current_sentence_start_time + estimated_speech_duration_seconds
        timed_sentences_with_ends.append((current_sentence_start_time, current_sentence_end_time, sentence))
        cumulative_time_seconds += estimated_speech_duration_seconds
        if i < len(sentences) - 1:
            cumulative_time_seconds += inter_sentence_silence_seconds
    return timed_sentences_with_ends, cumulative_time_seconds