from subprocess import Popen, PIPE

release_process = Popen(['python', '-m', 'fbs', 'release', '$Env:VERSION'], stdin=PIPE, stdout=PIPE)
# release_process.communicate(input=b'$Env:VERSION')