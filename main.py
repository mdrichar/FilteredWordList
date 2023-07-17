def create_bitset(letter_set, candidate):
    bitset = 0
    for i, letter in enumerate(letter_set):
        if letter in candidate:
            bitset |= 1 << i
    return bitset

letter_set = "abcde"
candidate = "bdg"

result = create_bitset(letter_set, candidate)
bitset_string = bin(result)[2:].zfill(12)
print(bitset_string)

from ListCoverage import ListCoverage

# letter_set=['inw','sco','rha','ekd']
letter_set = ['act','hbs','lrm','ido']
# letter_set = ['nhe','lug','arm','cot']
all_letters = "".join(letter_set)
print(all_letters)



import re
if re.match('abc','def'):
    print("YES")
else:
    print("NO")
    
import bak_main as wreader
wlist = wreader.get_filtered_list(all_letters)
final_list = wreader.get_sequence_filtered_list(wlist, letter_set)


def addCoverageTo(candidate, organizer):
    key = candidate.getKey()
    if key not in organizer:
        organizer_coverages = {}
        organizer[key] = organizer_coverages
    else:
        organizer_coverages = organizer[key]
                
    coverage = candidate.getCoverage()
    if coverage not in organizer_coverages:
        organizer_coverages[coverage]=candidate
    else:
        # There is already a word sequence with this coverage,
        # Only replace if it's an improvement
        existing_coverage = organizer_coverages[coverage]
        if existing_coverage.getUtility() > candidate.getUtility():
            organizer_coverages[coverage]=candidate

candidates = {}
for i, word in enumerate(wlist):
    # if i > 100:
    #     break
    # print(word)
    candidate = ListCoverage([word],all_letters)
    # print(candidate)
    addCoverageTo(candidate,candidates)
    # print(candidate)
    # key = candidate.getKey()
    # if key not in candidates:
    #     coverages = {}
    #     candidates[key] = coverages
    # else:
    #     coverages = candidates[key]
    
    # coverage = candidate.getCoverage()
    # if coverage not in coverages:
    #     coverages[coverage]=candidate
        
# for key, coverages in candidates.items():
#     print(key)
#     for coverage, lc in coverages.items():
#         print(coverage,lc)

def addsKeyTo(candidate, existing_coverages):
    return candidate.getKey() not in existing_coverages

def addsCoverageTo(candidate, existing_coverages):
    return candidate.getKey() in existing_coverages and candidate.getCoverage() not in existing_coverages[candidate.getKey()]

def improvesUpon(candidate, existing_coverages):
    key = candidate.getKey()
    if key not in existing_coverages:
        return False
    existing_for_key  = existing_coverages[key]
    candidate_coverage_amt = candidate.getCoverage()
    assert (candidate_coverage_amt in existing_for_key)
    existing_coverage = existing_for_key[candidate_coverage_amt]
    return candidate.getUtility() > existing_coverage.getUtility()

def augment(candidates, new_candidates):
    for key, new_coverages in new_candidates.items():
        for coverage_amt, new_coverage in new_coverages.items():
            addCoverageTo(new_coverage, candidates)
            
def totalSize(candidates):
    cnt = 0
    for v in candidates.values():
        cnt += len(v)
    return cnt

def compute(candidates):
    bestCoverageCnt = 0
    cnt = 0
    new_candidates = {}
    for key1, coverages1 in candidates.items():
        print(key1)
        for key2, coverages2 in candidates.items():
            if key1 != key2 and key1[1] == key2[0]:
                for cov1 in coverages1.values():
                    for cov2 in coverages2.values():
                        # Same first letter as first; same last letter of second
                        new_key = key1[0], key2[1]
                        lc = cov1.withAppended (cov2)
                        if lc.getCoveredLetterCnt() > bestCoverageCnt:
                            print(lc)
                            bestCoverageCnt = lc.getCoveredLetterCnt()
                        if lc.getCoveredLetterCnt() == 12:
                            return
                        addCoverageTo(lc,new_candidates)
                        # if new_key not in candidates:
                        #     print("New possible key: ",new_key)
                        #     print(lc)
                        #     assert(addsKeyTo(lc,candidates))
                        #     addCoverageTo(lc,new_candidates)
                        # else:
                        #     assert(not addsKeyTo(lc,candidates))
                        #     print("Existing key")
                        #     existing_key_coverages = candidates[new_key]
                        #     coverage_set = lc.getCoverage()
                        #     if coverage_set in existing_key_coverages:
                        #         assert(not addsCoverageTo(lc,candidates))
                        #         print("Existing coverage, need to compare")
                        #         existing_coverage = existing_key_coverages[coverage_set]
                        #         print(f"{existing_coverage} against {lc}")
                        #         if improvesUpon(lc,candidates):
                        #             print("Yes -- improves")
                        #         else:
                        #             print("No -- does not improve")
                        #     else:
                        #         assert(addsCoverageTo(lc,candidates))
                        #         addCoverageTo(lc,new_candidates)
                        #         print("New coverage possibility")
                        #         print(lc)
                        # cnt += 1
                        # print(key1,key2)
                        # if cnt > 10:
                        #     return
    print("Size before: ",totalSize(candidates))
    print("New candidates size: ",totalSize(new_candidates))
    
    augment(candidates, new_candidates)
    print("Size after: ",totalSize(candidates))
                        
# compute(candidates)