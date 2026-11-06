---
title: Open Slot AI, a Tulsa pitch
type: pitch
length: 8 min
rate: 140 wpm
audience: startup judges, operators, and investors at a pitch competition
thesis: When a Tulsa tech is on a unit, the next customer calls and nobody answers. Open Slot is an AI receptionist that speaks the booking only after Google Calendar returns an event id, and the ask is ten local owner conversations plus a hard read on a proposed $149 a month.
through-line: one call's state, scored 0 missed, 2 answered, 3 ready to write, 2 held because the calendar did not confirm, then 4 only after a real event id
bookend: the promise on slide 1 closes on BOOKED on the ask slide, same place on the canvas, with the ask left up for questions
default-transition: camera
---

# Open Slot AI

## Where words live

| Layer | File | Audience |
|---|---|---|
| **On screen** | `deck.html` | Judges — headlines, numbers, 5–10 words max per beat |
| **You say** | This table + `Note` column | Your spoken script (Jack story, CallRail caveats) |
| **Presenter only** | `<aside class="notes">` in each slide | You in Presenter view (`P`) — never on the projector |

Problem slides 2–4 are **white, minimal**. Sources and disclaimers stay in **notes**, not on screen.

A competition pitch for a working prototype. No paying shops, no measured missed-call rate, no invented round. Scenes are scenes. The only green in the deck is a calendar write that returned an id.

Style: **Problem (slides 1–4)** `#F8FAFC` / `#0F172A` / `#10B981` / `#EF4444` (Inter). **Product onward** `#0B1220` dark — tear from problem. On-screen = 3-second read; you speak from Notes + this table. Schibsted Grotesk and IBM Plex Mono. The camera feeds down the pad inside a chapter and tears the sheet off between chapters. The phone morphs into the system, then the camera zooms into the calendar write. Four transitions, same grammar as the Tare demo: camera continues, tear is a new chapter, morph is the same object, zoom goes inside the write.

| # | Chapter | Title (a claim, one full sentence) | Steps | Visual | Transition | Through-line | Note |
|---|---|---|---|---|---|---|---|
| 1 | — | Open Slot AI — never miss a call or an opportunity | 0 | dark split hero: mascot + name + two-line promise | - | 0 | Say **Open Slot AI** out loud. Both headline lines. Then **Meet Jack** (3 clicks: ring → voicemail → next on Google). |
| 2 | I · Problem | Meet Jack | 3 | white · story timeline + photo · incoming chip on step 1 | camera | 0 | **On screen:** Meet Jack · 4 people · Tulsa HVAC · three beats. **You say** while clicking: Jack on a unit, line rings → voicemail → next on Google. Then plumber paragraph verbatim from notes (under sink / missed job / 11pm). Illustrative — not a customer. |
| 3 | | Jack isn't alone · 50M+ | 0 | white · hero stat · Home services chip highlighted | camera | 0 | One line bridge from Jack to platform. 50M+ CallRail 2025. Home services = our lane. |
| 4 | | Caller behavior · 82% · $161K | 0 | white · 3 stat cards + closing line | camera | 0 | Tie back to Jack. Say bullet 2 verbatim. **Tear to dark** — Solution chunk (~60–75s). |
| 5 | II · Solution | Open Slot AI — the solution | 0 | dark · centered mascot · name · one hook line · Answers/Talks/Books | tear | 2 | ~15s. Only brand: Open Slot AI. |
| 6 | | It's as simple as making a phone call | 3 | dark · 3 cards in a row | camera | 3 | ~15s. Three clicks on cards. |
| 7 | | See Open Slot AI work | 0 | demo centered | whip | 3 | ~30s. Post-demo Jack line in notes. |
| 8 | | Confirmation waits until the calendar returns an event id | 2 | mock: a dispatch slip that holds, then confirms | zoom | 2 | We are inside the write. Sam Ortiz and the 555 number are fiction, not a customer. The first state is a write in progress. Click: it fails. Holding. No event id. The caller has not been told they are booked. That is the reversal. A talking agent is not a booking. Click again: the calendar returns an id. The one on the slip is a stand-in. Only now does green appear. In the prototype, confirmation waits on that response. |
| 9 | | Urgent calls follow a rule the shop sets | 2 | diagram: a fork, routine books and urgent escalates | camera | 2 | Routine work takes the left branch and becomes a calendar event. Do not skip the right branch, because a judge will ask about a no-cool call at night or anything that sounds like an emergency. Click: urgent does not get a policy we wrote in a pitch. The shop defines what is urgent and which person gets the escalation. Click to show that branch. If they have not written the rule, we do not invent a polite one and hope. Say that plainly. We will not demo a gas-leak script we do not have. |
| 10 | IV · Why now | Voice, telephony, and the calendar can now finish the call | 1 | diagram: three shifts that meet on one line | tear | 2 | Refuse the AI-market slide if you feel one coming. Three plain facts. A voice model can stay on a phone call, not just a chat box. Twilio already terminates the number a small shop prints on its truck. Google Calendar is already the book a lot of these owners use. Click. The technician does not install anything and does not learn a login. The change sits on the line. That is why a two-person HVAC shop can use it, and why this was a bad product five years ago. |
| 11 | V · Traction | The prototype books a calendar event and paying shops stay at zero | 1 | number: a zero beside the five things the prototype actually does | camera | 4 | Read the zero before you apologize for it. Paying shops: none. Do not say pilots, letters of intent, or waitlist. We do not have them. Then walk the five checks, because this is the evidence we do have. Twilio answers. Vapi talks. We read availability. We create the event through the calendar API. We withhold the spoken booking when that call does not return an id. Click if you need the sentence: a build, not a business. If they ask for revenue, point at the zero and stop. |
| 12 | VI · Ask | The proposed price is one hundred forty-nine dollars a month | 1 | number: $149, labeled proposed and not charged | tear | 4 | One hundred forty-nine dollars a month is a proposal for a shop of one to ten people, HVAC and plumbing first. Click before anyone multiplies it by a market we have not counted. We have not charged it. We have no measured payback. A recovered service call might cover the month, and it might not, and we will not pretend we have that study. The ten conversations are how we find out if the price is even in the right band. |
| 13 | | We begin with shops we can drive to in Tulsa | 2 | diagram: map of later, Oklahoma, then Tulsa | camera | 4 | There is no total addressable market on this slide, and that is a choice. We do not have a counted list of Tulsa HVAC or plumbing shops, so we will not invent one. Click out from later, to Oklahoma, to Tulsa. Click again on the inner circle. HVAC first, plumbing next, teams of one to ten, a shop we can drive to and sit in. If they want a national number, say it is future work and it would be decoration tonight. |
| 14 | | Messages wait while Open Slot writes the appointment | 1 | diagram: 2x2 of categories, not named companies | camera | 4 | Categories, not a teardown of named companies. We have not earned a competitive grid with win rates. Voicemail keeps a recording. An answering desk usually takes a message. The owner books the job, but only when they are free to pick up. Click. Open Slot is the corner we are building toward: the calendar gets the appointment while the tech is still on the unit. Say we have not earned that corner with customers. We are showing where the product sits, not a share we hold. |
| 15 | | Ten owner conversations come before any national rollout | 3 | diagram: roadmap from the prototype to a paid month | camera | 4 | Today is already true: the prototype can book a test event. Click: the next mile is ten conversations with Tulsa owners, not a city launch. Click: design partners who put us on their real line and hand us their urgent rule. Click: a paid month, and only if those bookings hold. The later marks are a plan. They are not a forecast and they are not pipeline. Do not add a logo you have not signed. If the ten conversations say the call fails, the later marks move. |
| 16 | | We are asking for ten Tulsa owner conversations | 0 | number: the same handset, now booked, with the ask | tear | 4 | Leave this frame up for every question. The handset that opened on a miss now reads booked, and the id on the glass is a stand-in, not a customer record. The ask is ten introductions to owners of small HVAC or plumbing shops in Tulsa, and a hard read on whether one hundred forty-nine dollars is the right place to start. Put your real name and number on this slide before you walk in. Then stop talking. |


## Reference deck swipe (medical slides)

**Swipe:** layout (kicker, subhead, stat cards, behavior-shift headline), story order (pain → scale → behavior + money).

**Do not swipe onto the projector without sources:** 25–35% clinic unanswered, 75–80% / 87% voicemail, 1-in-3 hold (unless you cite the same study for trades), $100k dental practice. Open Slot uses **CallRail** + your **plumber paragraphs** only.
