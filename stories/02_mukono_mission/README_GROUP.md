# The Mukono Mission: Group Extensions

Group work for **The Mukono Mission** (`stories/02_mukono_mission`).

## Group members and extensions

Each member completes one different extension on their own branch.

| Member | Access number | Extension | Branch | Pull request |
|--------|---------------|-----------|--------|--------------|
|Malish Emmanuel Abui | b33239 | 5. Trip diary | `MALISH-EMMANUEL-ABUI-B33239-M25B13/032` | https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/2 |

| Mukisa Emmanuel| b30672 | 3. CousinLift | `mukisa-b30672` | https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/5 |

| Omara Chrispus Adrian  | B33146 | Extension 2: Transport money top_up | `OMARA-CHRISPUS-ADRIAN--B33146-M25B13/056` | https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/3 |

| WAGONDA FRANCIS PRECIOUS | B33245| Extension 1: Student shuttle | `WAGONDA-FRANCIS-PRECIOUS-B33245`| https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/1 |

| Kasozi Joel  | B33494 | Extension 4 : Cheapest ride | `joel-B33494` | https://github.com/MALISH-WEB/Mission-impossible-Mukono-Mission/pull/4 |


## The six extensions

1. **Student shuttle:** a `Shuttle` subclass of `Transport` that quotes UGX 1,500 for any positive distance. It works in `compare()` and `travel()` without changing them.
2. **Transport money top-up:** `top_up(amount)` on `TripPurse`. A positive amount adds money and returns `True`. Zero or a negative amount returns `False` and changes nothing.
3. **A lift from a cousin:** `CousinLift`, which does not inherit from `Transport`. It has `name`, `describe()` and `quote_fare(distance)` returning 0, and works through `compare()` and `Journey.travel()`.
4. **Cheapest ride:** `cheapest(options, distance)` returns the cheapest option, or `None` for an empty list. For equal fares it keeps the first option.
5. **Trip diary:** `diary()` on `Journey` returns the completed transport names, the completed-leg count and the money left. It does not count refused attempts or spend money.
6. **Rainy-day boda:** `RainyDayBoda`, a subclass of `Boda`, adds UGX 1,000 to `super().quote_fare(distance)`. It works through the existing loop and `Journey`.

## Rules every member followed

- The original classes and behaviour still work, and the original `main()` story is unchanged.
- Each new class or method has a short explanatory comment.
- Each member has their own demo file beside `story.py`, named `demo_<firstname>_<accessnumber>.py`.
- Each demo shows one normal case and one refused, empty or boundary case, and prints what we expect and what actually happens.
- Each demo uses separate objects so one check does not affect another.

