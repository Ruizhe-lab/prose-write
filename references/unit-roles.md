# Unit roles, with invented examples

Every unit has one job, and the job decides its first sentence.
Use this with the card in [the unit file](unit-plan-card-gate.md), "The card". The table of roles is there; this file only illustrates it.
The examples are invented for teaching. They come from no real paper. They use one imaginary study: outpatient clinics that book more patients than they have slots, and what happens when they start sending appointment reminders.

## 1. Opening that carries a surprise

The job: give the reader the expectation, the finding that contradicts it, and the route. The mechanism waits for the body.

Weak:

> This section studies reminders. Reminders reduce missed appointments. Clinics overbook. Waits rise because attendance exceeds the number of slots when the booking level is unchanged, as a queueing model with two patient types shows.

Better:

> A clinic that reminds patients of their appointments should run closer to schedule. Fewer slots go unused, and staff spend less time idle. In the twelve clinics we study, waits grew instead. The rest of the section traces the cause to a booking rule that the clinics left as it was.

What to notice:
- The expectation comes with its reason, so the reader holds it before it fails.
- The finding takes one short sentence.
- The cause is named and not explained. An opening that explains the whole mechanism leaves the body nothing to do.

## 2. Opening of a derivation

The job: say what is being solved and why, before any display.

Weak: "The clinic's objective is given by the following expression."

Better: "We now find the number of bookings that costs a clinic least. An extra booking makes an empty slot less likely and an overfull session more likely, and the clinic weighs one against the other." The display follows, and one sentence reads each of its terms.

## 3. Setup

The job: state the rules once, in words, then the notation, in a separate paragraph.

> A clinic runs one session a day with a fixed number of slots. Before the session it decides how many patients to book. Each booked patient either attends or misses, independently of the others. Patients who attend are seen in order of arrival. When more attend than there are slots, the session runs over.
>
> Let n be the number of slots, b the number of bookings, and m the probability that a booked patient misses.

What to notice: the first paragraph can be read without a symbol, and it computes nothing. How the clinic chooses b belongs to the results.

## 4. The means (solving)

The job: reach the result with the least machinery.

State in one sentence the problem the agent solves. Display only the condition the text goes on to read. Send the algebra to the appendix.

> The clinic adds bookings until the expected cost of one more overfull slot equals the expected saving from one fewer empty slot. Equation (3) states this balance.

The intermediate displays that lead to equation (3) do not appear in the main text.

## 5. Explanation after a result

The job: make the reader understand the result. Restating its conditions does not do that.

Restating:

> The optimal booking level increases in the miss rate and decreases in the cost of waiting, as equation (3) shows.

Explaining:

> A clinic whose patients often miss can book well beyond its slots, because most sessions will still have room. As attendance becomes reliable, each extra booking is more likely to bring a patient for whom no slot is free, and the clinic should book fewer. Reminders move a clinic from the first situation towards the second. Its waits lengthen when nobody revisits the booking level.

## 6. The part that carries the point

The job: one case the reader can picture, then the general statement.

> Take a session with twenty slots and twenty-four bookings. When one patient in six misses, twenty attend on average and the session ends on time. With reminders, one in twelve misses, twenty-two attend, and the last two are seen after the session should have closed. In general, a booking level set for the old miss rate brings more patients than slots once attendance improves.

If an equation carries the point, give it a short formal statement and explain it afterwards.

## 7. Confirmation or test

The job: state the prediction, then what the data show. Do not dress a predicted result as a surprise.

Right frame: "The model predicts longer waits only in clinics that kept their booking level. The appointment records let us check."
Wrong frame: "Remarkably, waits rose in clinics that kept their booking level."

## 8. Light edit, and no change

The job: leave a sound chain alone.

Replace a loose word ("show up more" becomes "attend more often") or correct a reference that points to the wrong table. Leave the order and the sentences as they are.
In a coauthor's section, or a part the author calls fine, the answer is often "no change", with one material issue if there is one ([the team file](../HOW_WE_WORK.md), MATERIAL-NOT-WORDING).
