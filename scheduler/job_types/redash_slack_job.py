"""A job to run executable programs."""
import logging

from subprocess import Popen, PIPE

from ndscheduler import job

logger = logging.getLogger(__file__)

class RedashEmailSummary(job.JobBase):

    @classmethod
    def meta_info(cls):
        return {
            'job_class_string': '%s.%s' % (cls.__module__, cls.__name__),
            'arguments':[
                {'type': 'string', 'description': 'Executable path'}
            ],
            'notes': ('This will send scheduled email alerts for your redash query'),
            'example_arguments': '["-q 5326 -c CET024BAP"]'
        }

    @staticmethod
    def execute_command(args):
        args = "cd /redash-summary/ && /redash-summary/venv/bin/python send_slack.py " + args[0]
        p = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        stdout, stderr = p.communicate()
        return_code = p.returncode

        logger.debug("stdout: {}".format(stdout))
        logger.debug("stderr: {}".format(stderr))
        logger.debug("return_code: {}".format(return_code))

        return stdout.decode('utf-8'), stderr.decode('utf-8'), return_code

    def run(self, *args, **kwargs):
        stdout, stderr, return_code = self.execute_command(args)

        return {
            'return_code': return_code,
            'stdout': stdout,
            'stderr': stderr
        }


if __name__ == "__main__":
    # You can easily test this job here
    job = ShellJobWithLogs.create_test_instance()
    logger.info('Job instance created')
    result = job.run('ls', '-l')
    logger.info('Output: {}'.format(result))
