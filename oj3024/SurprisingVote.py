"""หาคะแนนที่ต่ำที่สุด"""

score = float(input())
pscore = float(input())
leftscore = score - pscore
minscore = leftscore - pscore

if minscore < 0:
    minscore = 0.0

if (pscore - minscore) > 2 :
    print("Surprising")
else :
    print("Not surprising")
