# Group submission

- Group number / catch-up label: Mission Impossible
- Story: The Mukono Mission
- Group fork URL: https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission
- Final branch: `main`
- Deadline: end of Wednesday, 21 October 2026, Uganda time

## Members and foundation work

| Full name | Access number | Registration number | GitHub username | Foundation task | Personal branch | Commit link(s) | Merged foundation PR |
|---|---|---|---|---|---|---|---|
| Wagonda Francis Precious | B33245 | M25B13/038 | franciswagonda | Extension 1: Student shuttle | [WAGONDA-FRANCIS-PRECIOUS-B33245](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/tree/WAGONDA-FRANCIS-PRECIOUS-B33245) | [commits](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/commits/WAGONDA-FRANCIS-PRECIOUS-B33245/) | [PR 1](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/1) |
| Malish Emmanuel Abui | B33239 | M25B13/032 | MALISH-WEB | Extension 5: Trip diary (`Journey.diary`) | [MALISH-EMMANUEL-ABUI-B33239-M25B13/032](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/tree/MALISH-EMMANUEL-ABUI-B33239-M25B13/032) | [commits](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/commits/MALISH-EMMANUEL-ABUI-B33239-M25B13/032/) | [PR 2](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/2) |
| Omara Chrispus Adrian | B33146 | M25B13/056 | omara-chrispus-adrian | Extension 2: Transport money top-up (`TripPurse.top_up`) | [OMARA-CHRISPUS-ADRIAN--B33146-M25B13/056](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/tree/OMARA-CHRISPUS-ADRIAN--B33146-M25B13/056) | [commits](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/commits/OMARA-CHRISPUS-ADRIAN--B33146-M25B13/056/) | [PR 3](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/3) |
| Kasozi Joel | B33494 | M25B13/051 | KasoziJoel | Extension 4: Cheapest ride | [joel-B33494](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/tree/joel-B33494) | [commits](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/commits/joel-B33494/) | [PR 4](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/4) |
| Mukisa Emmanuel | B30672 | TO FILL | TO FILL | Extension 3: A lift from a cousin (`CousinLift`) | [mukisa-b30672](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/tree/mukisa-b30672) | [commits](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/commits/mukisa-b30672/) | [PR 5](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/5) |

## Three later-topic choices

| Selected option | Members and specific responsibilities | Merged later-topic PRs | Demo command | Automated-check command |
|---|---|---|---|---|
| A1: Values that can print, compare and add | Kasozi Joel: `FareMoney` with `__str__`, `__repr__`, `__eq__`, `__add__`, and the fare preview | [PR 6](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/6) | `py -3 A1-b33494.py` | TO FILL |
| A2: Errors the story can explain | Mukisa Emmanuel: the three custom exceptions and `StrictJourney.safe_travel` in `story.py`. Malish Emmanuel Abui: the A2 demo and the automated tests (`test_a2_strict_journey.py`) | [PR 7](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/7) (Emmanuel's demo), [PR 8](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/8) (Mukisa), TO FILL (A2 code in `story.py` and tests) | `py -3 "stories/02_mukono_mission/Demo a2 emmanuel b33239.py"` | `py -3 -m unittest discover -s stories/02_mukono_mission -p "test_*.py"` |
| A3: Save the story and continue later | Wagonda Francis Precious: `Journey.save` / `Journey.load` and 19 automated tests. Omara Adrian Chrispus: the save and load demo | Francis: https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/9         Adrian : | `py -3 stories/02_mukono_mission/demo_save_load_adrian_b33146.py` | `py -3 -m unittest discover -s stories/02_mukono_mission -p "test_*.py"` |

## Individual later-topic contributions and reviews

| Member | Later-topic responsibility | Personal branch | Commit link(s) | Merged later-topic PR(s) | Review/comment links on teammates' PRs |
|---|---|---|---|---|---|
| Wagonda Francis Precious | A3: save/load code and tests; restored the original `main()` | WAGONDA-FRANCIS-PRECIOUS-B33245 | https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/commit/053864ccde9cde9a8e14533f75697ac8e7a9c436  | https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/9 | https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/8#issuecomment-6443912882   https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/7#issuecomment-6443876618   https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/6#issuecomment-6443983602 |
| Malish Emmanuel Abui | A2: demo and automated tests | MALISH-EMMANUEL-ABUI-B33239-M25B13/032 | [commit f35ebca](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/commit/f35ebca) | [PR 7](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/7) | https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/2#issue-5852824773  |
| Omara Chrispus Adrian | A3: save and load demo | OMARA-CHRISPUS-ADRIAN--B33146-M25B13/056 |https://github.com/slubambo/ucu-oop-class-examples/commit/2cb4d88af71a97982467cc84461629ad9d44a29e#diff-82ca9cebaef0fd14989189f17fd4a5cb9f40df25cf0799a0e37674c4bd9d116d|https://github.com/slubambo/ucu-oop-class-examples/pull/81 | TO FILL |
| Kasozi Joel | A1: `FareMoney` and fare preview | joel-B33494 | [commit ee6bf79](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/commit/ee6bf79) | [PR 6](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/6) | TO FILL |
| Mukisa Emmanuel | A2: custom exceptions and `StrictJourney` in `story.py`; restored the Extension 3 demo | mukisa-b30672 | [commit 9cad536](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/commit/9cad536) | [PR 8](https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/8) | TO FILL |

## Explain the work

**A1: printable, comparable values.** Fares are plain numbers, so a total or a fare could be confused with any other number. `FareMoney` wraps a whole number of UGX and refuses negatives, fractions and Booleans. `__str__` gives the friendly form (UGX 3,000), `__repr__` gives the developer form (`FareMoney(3000)`), `__eq__` compares amounts, and `__add__` returns a new `FareMoney` without changing either original. For unsupported operands these methods return `NotImplemented`. `preview_total(choices, distance)` asks each choice for its fare and returns the combined total without spending anything.

**A2: errors the story can explain.** Three exceptions describe why a trip cannot happen: `JourneyChoiceError` (no usable choice), `JourneyRequestError` (bad distance or negative fare) and `JourneyResourceError` (not enough UGX). `StrictJourney.safe_travel` checks the request first, raises the matching error, and only then calls the normal `Journey.travel`, so a refused request never spends money or records a leg.

**A3: save and continue later.** `Journey.save(path)` writes the student, remaining UGX and the completed legs as plain JSON. `Journey.load(path)` checks the whole file first and only then returns a new `Journey` with a fresh purse and fresh choice objects. Choices are rebuilt from a fixed table of labels (boda, taxi, shuttle, student_boda, cheerful_student_boda, cousin_lift, walk_with_friend), so nothing from a file is ever run. A missing file raises `FileNotFoundError`. Bad JSON, wrong types, extra or missing keys, a wrong version, a negative balance or an unknown label raise `ValueError`, and a failed load never changes a session that is already running. 19 automated tests use temporary files to check normal, boundary and refused cases.

**Connection with the foundation features.** A3 saves and restores the shuttle (Extension 1) and the cousin lift (Extension 3), and the restored journey keeps the same money rules as `TripPurse`. A2's `StrictJourney` is a subclass of `Journey`, so the original `travel` keeps working.

## Run the final project

From the main repository folder (on Windows use `py -3`; on macOS or Linux use `python3`):

- Original story: `py -3 stories/02_mukono_mission/story.py` (matches `expected_output.txt`)
- Foundation demos:
  - `py -3 stories/02_mukono_mission/demo_francis_b33245.py`
  - `py -3 stories/02_mukono_mission/demo_emmanuel_b33239.py`
  - `py -3 stories/02_mukono_mission/Demo_Adrian_B33146.py`
  - `py -3 stories/02_mukono_mission/demo_mukisa_b30672.py`
  - `py -3 demo-Joel-B33494.py`
- Later-topic demos: see the table above.
- Automated checks: `py -3 -m unittest discover -s stories/02_mukono_mission -p "test_*.py"`

Result on final `main`: TO FILL (number of tests run, and OK or failures).

## Group evaluation (maximum 250 words)

We built the Mukono Mission extensions as a group of five. Each member added one foundation feature: a student shuttle, a money top-up, a cousin lift, a cheapest-ride finder and a trip diary. For the later topics we chose A1, A2 and A3.

The OOP ideas we used were inheritance and abstract classes (the shuttle is a Transport), duck typing (the cousin lift has no parent class), encapsulation (the purse protects its balance), composition (a Journey owns a purse), dunder methods (FareMoney), custom exceptions (StrictJourney) and JSON saving with a fixed table of allowed labels, so nothing from a file is run.

What worked well was keeping the original story unchanged and showing every feature in its own demo, and writing tests that check normal, boundary and refused cases.

Our main difficulty was working in one shared file. Someone added a cousin lift to the original main(), which broke the original expected output, and we had to restore it. Line endings (Windows and Linux) also made one pull request look like the whole file had changed, so we converted the files and checked the diff before merging.


Word count: 236

## Final check

- [ ] All required foundation tasks work on `main`.
- [ ] Exactly three later-topic choices are nominated and work together.
- [ ] Every member has merged foundation and later-topic PR evidence.
- [ ] Each PR has useful comments from all its author's teammates before merge.
- [ ] The original story still runs and matches the original expected output.
- [ ] All demos and automated checks run from final `main`.
- [ ] All members are listed with full names, access numbers, registration numbers and GitHub usernames.
- [ ] The story title, individual commits, PRs and review links are complete.
- [ ] The group evaluation is no more than 250 words.
- [ ] Every member can explain their own work.
