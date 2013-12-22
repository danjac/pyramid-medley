import freezegun

def test_job_is_run():

    from ..scripts.crons import run_jobs
    from ..scripts.crons.base import job

    jobs_run = []

    @job(minute=0)
    def check_run(env):
        jobs_run.append("check_run")

    with freezegun.freeze_time('2013-12-22 12:00'):
        run_jobs({})

    assert "check_run" in jobs_run


def test_job_is_not_run():

    from ..scripts.crons import run_jobs
    from ..scripts.crons.base import job

    jobs_run = []

    @job(minute=0, month=6)
    def check_run(env):
        jobs_run.append("check_run")

    with freezegun.freeze_time('2013-12-22 12:00'):
        run_jobs({})

    assert "check_run" not in jobs_run
