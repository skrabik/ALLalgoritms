n = int(input())
years = list(map(int, input().split()))
X = years[-1]

periods = []
remainingYears = set(years)

while remainingYears:
    bestPeriod = 1
    bestCovered = set()
    
    candidatePeriods = set()
    candidatePeriods.add(1)
    
    for year in remainingYears:
        if year > 1:
            num = year - 1
            i = 1
            while i * i <= num:
                if num % i == 0:
                    if i <= X:
                        candidatePeriods.add(i)
                    divisor = num // i
                    if divisor <= X:
                        candidatePeriods.add(divisor)
                i += 1
    
    for period in candidatePeriods:
        coveredByPeriod = set()
        for year in remainingYears:
            if (year - 1) % period == 0:
                coveredByPeriod.add(year)
        
        if len(coveredByPeriod) > len(bestCovered):
            bestPeriod = period
            bestCovered = coveredByPeriod
    
    periods.append(bestPeriod)
    remainingYears -= bestCovered

print(len(periods))
