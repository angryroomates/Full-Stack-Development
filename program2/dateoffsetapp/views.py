from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def dateoffset(request):
    now = datetime.now()
    offset_day = timedelta(days=4)
    offset_hours = timedelta(hours=4)
    p_day = now + offset_day
    m_day = now - offset_day
    p_hour = now + offset_hours
    m_hour = now - offset_hours
    context = {"date": now.date, "time": now.time, "p_day": p_day, "m_day": m_day, "p_hour": p_hour, "m_hour": m_hour, "day": 4}
    return render(request, 'dateoffset.html', context)

def dateoffsetnum(request, offset):
    var = offset
    now = datetime.now()
    offset_day = timedelta(days=var)
    offset_hours = timedelta(hours=var)
    p_day = now + offset_day
    m_day = now - offset_day
    p_hour = now + offset_hours
    m_hour = now - offset_hours
    context = {"date": now.date, "time": now.time, "p_day": p_day, "m_day": m_day, "p_hour": p_hour, "m_hour": m_hour, "day": var}
    return render(request, 'dateoffset.html', context)