import ansible.runner
import ansible.playbook
from ansible import callbacks
from ansible import utils

stats = callbacks.AggregateStats()
playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
runner_cb = callbacks.PlaybookRunnerCallbacks(stats,
verbose=utils.VERBOSITY)


pb = ansible.playbook.PlayBook(
     playbook="test.yml",
     stats=stats,
     callbacks=playbook_cb,
     runner_callbacks=runner_cb,
     check=True
)
for (play_ds, play_basedir) in zip(pb.playbook, pb.play_basedirs):
     import ipdb
     ipdb.set_trace()
     # Can play around here to see what's going on.


pb.run() # This runs the playbook
