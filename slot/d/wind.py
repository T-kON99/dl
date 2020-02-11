from slot import *

class Zephyr(DragonBase):
    ele = 'wind'
    att = 127
    a = [('a', 0.6)]

class Pazuzu(DragonBase):
    ele = 'wind'
    att = 127
    a = [('k_poison', 0.2), ('a', 0.5)]

class Long_Long(DragonBase):
    ele = 'wind'
    att = 127
    a = [('a', 0.45), ('cd', 0.55)]

class Freyja(DragonBase):
    ele = 'wind'
    att = 120
    a = [('sp', 0.35)]

class Vayu(DragonBase):
    ele = 'wind'
    att = 127
    a = [('s', 0.9), ('a', 0.2)]
    dragonform = {
        'act': 'c3 s',

        'dx1.dmg': 2.08,
        'dx1.startup': (16+19) / 60.0, # c1 frames
        'dx1.recovery': 34 / 60.0, # c2 frames
        'dx1.hit': 2,

        'dx2.dmg': 2.26,
        'dx2.recovery': 79 / 60.0, # c3 frames
        'dx2.hit': 1,

        'dx3.dmg': 3.69,
        'dx3.recovery': 40 / 60.0, # dodge frames, real recovery 80
        'dx3.hit': 1,

        'ds.recovery': 100 / 60, # skill frames
        'ds.hit': 1,
    }

    def oninit(self, adv):
        super().oninit(adv)
        from adv import SingleActionBuff
        self.ds_buff = SingleActionBuff('d_sd_buff',0.40,1,'s','buff')

    def ds_proc(self):
        dmg = self.adv.dmg_make('d_ds',8.96,'s')
        self.ds_buff.on(1)
        return dmg

class Hastur(DragonBase):
    ele = 'wind'
    att = 127
    a = [('primed_att', 0.15), ('a', 0.45)]

class Garland(DragonBase):
    ele = 'wind'
    att = 127
    a = [('a', 0.5)]

    def oninit(this, adv):
        DragonBase.oninit(this, adv)
        this.adv = adv
        if adv.condition('maintain shield'):
            adv.Timer(this.dauntless_rampart).on(15)

    def dauntless_rampart(this, t):
        this.adv.Buff('dauntless_rampart',0.30,-1,'att','passive').on()

class Unreleased_DKR_Baby_dont_hurt_me(DragonBase):
    ele = 'wind'
    att = 127
    a = [('a', 0.55), ('fs', 0.60), ('sp',0.30,'fs')]