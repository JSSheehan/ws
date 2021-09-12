## Features Todo List

#### Done
- worlds played
- num correct
- num incorrect
- time as player
- num assessments

#### TODO
- [ek] mean time in an assessment (exclude outliers?)
- [ek] cumulative time playing the game?
- [ek] installation duration mean (what does this mean? same as above?)
- [ek] accuracy of game/activity directly prior to the assessment
- [ek] accuracy of all games/activities prior to the assessment and after last assessment
- [ar] has it been a long gaming session?
- [ar] "exit_type":"game_completed" -- if a player has any other exit types, they are a bad player
- [ar] event_id=cdd22e43 -- this event could show a player is unskilled
- [ar] num events divided by num assessments
- [ar] num game sessions
- [ar] num playing sessions
- [ss] time in current playing session
- [ss] time of day
- [ss] time of day compared to user's "normal" time of play
- [ss] name of assessment
- [ss] has the player played this assessment before
- [ch] number of clicks to perform an action
- [ch] number of "wild" clicks (many clicks in quick succession)
- [ch] length of current playing session
- [ch] phase of day (morning, afternoon, night)
- [mc] phase of day compared to normal phase of day for that player
- [mc] weekend?
- [mc] during school hours?
- [mc] event data: "misses"
- [mc] event data: "misses" divided by total events in that activity
- [ch] activity duration vs. mean duration for that activity in entire train set (calculate means beforehand)
- [ch] event counts to complete activity vs. mean event counts for that activity in entire train set (calculate means beforehand)
- num correct/incorrect vs. mean num correct/incorrect for that activity in entire train set (calculate means beforehand)
- activity duration vs. median duration for that activity in entire train set (calculate medians beforehand)
- event counts to complete activity vs. median event counts for that activity in entire train set (calculate medians beforehand)
- num correct/incorrect vs. median num correct/incorrect for that activity in entire train set (calculate median beforehand)
- screen size or type of device (using "stage_width" and "stage_height")
- event types showing lack of skill: bc8f2793, cdd22e43, 3d63345e, d02b7a8e, 363c86c9, c58186bf, d38c2fd7, 9ce586dd, d3f1e122, 0d18d96c, d185d3ea, a2df0760, 3edf6747, 
- average accuracy group for this assessment
- median accuracy group for this assessment
- events that say "(Correct)" or "correctly" (be careful not to include ones that only say "incorrect")
- events that say "(Incorrect)" or "incorrectly"
