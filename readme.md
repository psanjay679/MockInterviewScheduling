### Requirements

- The Interviewers provide their own availability. They are not available 24/7 for any slot that the student requests. 

- A student should not be able to see any interviews if they have already completed their 15

- A student should only see slots from an interviewer who has not interviewed the student before.

- A student should only see additional interviews if they have not given an interview before or their last 2 interview grades are > 1. (We have a grading scale from 0 - 5). 


The input request looks like this

```
{
	"studentId": 123,

	"startDateTime": "2020-06-05T13:00:00",

	"endDateTime": "2020-06-05T14:00:00",
}

```

### Classes

- Student (id, name, email, phone, Address, Sessions)
- Address (pin, street, city, state, country)
- Interviewer (id, name, email, phone, Address, Sessions)
- Session (id, SessionStatus, rating)
- Slot (start_time, end_time)
- SessionStatus (PENDING, COMPLETED, CANCELED, RESCHEDULED)
- Constants (MAX_SESSIONS_PER_STUDENT=15)