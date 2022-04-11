### Attack & release FX in Foxdot
### add this to /FoxDot/lib/Effects/Util.py

fx = FxList.new("a", "adsr", {"a":0, "r":1, "sus": 1, "ac": 0, "rc": 0}, order=2)
fx.add_var("env")
fx.add("env = EnvGen.ar(Env.new(levels: [0,1,1,0], times:[a*sus, max((a*sus + r*sus), sus - (a*sus + r*sus)), r*sus], curve:[ac,0,rc]))")
fx.add("osc = osc*env")
fx.save()

# a1 >> pluck(lpf=4000, oct=(3,4,5), dur=8, a=PWhite(0,1), r=PWhite(0,1), ac=PWhite(-12,12), rc=PWhite(-12,12))
