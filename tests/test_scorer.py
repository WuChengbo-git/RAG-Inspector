from backend.app.services.scorer import Scorer


def test_retrieval_accuracy() -> None:
    s = Scorer()
    score = s.retrieval_accuracy(['a', 'b'], ['b', 'c'])
    assert score == 0.5


def test_answer_quality() -> None:
    s = Scorer()
    score = s.answer_quality('hello world', 'world hello hi')
    assert score == 1.0


def test_combine_scores() -> None:
    s = Scorer()
    es = s.combine_scores('q1', 0.5, 1.0)
    assert es.question_id == 'q1'
    assert es.score == 0.75
