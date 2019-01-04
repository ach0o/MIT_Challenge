============================================
An Exam Scheduling(*Graph Coloring*) Problem
============================================
*Graph Coloring Problem*: Given a graph G, assign colors to each node such that adjacent nodes have different colors.

Each term, the MIT Schedules Office must assign a time slot for each final exam. This is not easy, because some students are taking several classes with finals, and (even at MIT) a student can take only one test during a particular time slot. The Schedules Office wants to avoid all conflicts. Of course, you can make such a schedule by having every exam in a different slot, but then you would need hundreds of slots for the hundreds of courses, and the exam period would run all year! So, the Schedules Office would also like to keep exam period short.

The Schedules Office's problem is easy to describe as a graph. There will be a vertex for each course with a final exam, and two vertices will be adjacent exactly when some student is taking both courses.

...The main constraint is that *adjacent vertices must get different colors*--otherwise, some student has two exams at the same time. Furthermore, in order to keep the exam period short, we should try to color all the vertices using *as few different colors as possible*.

Taken from Chapter 5 Graph Theory(p.144) of the lecture note provided by MIT(https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2010/readings/)
