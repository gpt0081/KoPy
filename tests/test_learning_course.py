"""기본 CI에서 공식 학습 코스 무결성 테스트를 함께 실행합니다."""

from 학습_코스.테스트.test_course import CourseExecutionTests, CourseStructureTests


__all__ = ["CourseExecutionTests", "CourseStructureTests"]
