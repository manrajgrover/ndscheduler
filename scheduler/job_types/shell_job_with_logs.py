"""A job to run executable programs."""
import logging
import base64

from subprocess import Popen, PIPE

from ndscheduler import job

logger = logging.getLogger(__file__)

class ShellJobWithLogs(job.JobBase):

    @classmethod
    def meta_info(cls):
        return {
            'job_class_string': '%s.%s' % (cls.__module__, cls.__name__),
            'notes': ('This will run an executable program. You can specify as many '
                      'arguments as you want. This job will pass these arguments to the '
                      'program in order.'),
            'arguments': [
                {'type': 'string', 'description': 'Executable path'}
            ],
            'example_arguments': '["/usr/local/my_program", "--file", "/tmp/abc", "--mode", "safe"]'
        }

    @staticmethod
    def execute_command(args):
        p = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        stdout, stderr = p.communicate()
        return_code = p.returncode

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
