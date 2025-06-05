from backend.app.services.reporter import Reporter
from backend.app.models import EvaluationScore


def test_to_csv(tmp_path) -> None:
    reporter = Reporter(tmp_path)
    scores = [EvaluationScore(question_id='q1', score=0.9)]
    path = reporter.to_csv(scores, 'result.csv')
    assert path.exists()
    content = path.read_text()
    assert 'q1' in content
