if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
from adv import *
from slot.a import *

def module():
    return Renelle

class Renelle(Adv):
    a1 = ('cc',0.15,'hit15')
    conf = {}
    conf['cond_afflict_res'] = 0
    conf['slot.a'] = TB()+EE()
    conf['acl'] = """
        `rotation
        """
    conf['rotation_init'] = """
        c4fs C4FS C1- 
    """
    conf['rotation'] = """
        S1 C4FS C4FS C1- S1 C1- S2 C4FS C5- S1 C1- S3
        C4FS C5- S1 C2- S2 C4FS C5- S1 C4FS C4FS C1- S1 C1- S3 C1- S2 C4fs !c5!
    """

    def prerun(this):
        if this.condition('{} resist'.format(this.conf['cond_afflict_res'])):
            this.afflics.burn.resist=this.conf['cond_afflict_res']
        else:
            this.afflics.burn.resist=100

    def s1_proc(this, e):
        this.afflics.burn('s1',100,0.803)
    
    def s2_proc(this, e):
        this.afflics.burn('s2',90,0.6)

    def rinit(this):
        this.rotation('')

if __name__ == '__main__':
    conf = {}
    # why c4fs at end, not c5
    adv_test.test(module(), conf, verbose=-2)

