import string
import random


class FilterModule(object):
  ''' Eyeota Ansible filters '''

  def filters(self):
        
    return {
      'generate_vm_name':self.generate_vm_name,
    }

  def generate_vm_name(self, group, length=8):
    name = str(group)+'-'+''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(length)])
    return name