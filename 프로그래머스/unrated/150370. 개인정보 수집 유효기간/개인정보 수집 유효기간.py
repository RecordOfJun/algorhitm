def solution(today, terms, privacies):
    answer = []
    term_list=dict()
    t_year,t_month,t_day=map(int,today.split("."))
    t_total=t_year*12*28+t_month*28+t_day
    for i in range(len(terms)):
        term,length=map(str,terms[i].split(" "))
        term_list[term]=int(length)
        
    for i in range(len(privacies)):
        date,term=map(str,privacies[i].split(" "))
        year,month,day=map(int,date.split("."))
        total=year*12*28+month*28+day+term_list[term]*28
        if total<=t_total:
            answer.append(i+1)
    answer.sort()
    return answer