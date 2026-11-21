# Lesson format and syllabus authoring

## Format
Each lesson is a 4-tuple, exactly as stored in the app's `LS` object:
`["Lesson title", hours, "Learn: ... Do: ...", "Resource 1; Resource 2"]`
- Title: short and specific. Hours: usually 3 to 6.
- Description: start with what to learn (concepts, why they matter later), then what to do (a problem count or a concrete deliverable, e.g. "derive it", "plot it in Python"). Include a self-check where useful.
- Resources: free, real, specific (course and unit, episode number, chapter number).
- Lessons for a module must **sum exactly to the module's hours** in the app's `T` array, in the order a learner should do them.
- Keys of `LS` are the exact task titles used in `T` (for example "Calculus completion + vectors").

## Syllabus status
Written (in `assets/frontierpath.html`, object `LS`): Diagnostic and setup (5 h), Calculus completion + vectors (50 h), Newtonian mechanics refresh (30 h), Multivariable calculus (50 h). That covers about the first 4.5 weeks.

Still to write, in this order, with resource hints:
1. Linear algebra (60 h): 3Blue1Brown Essence of Linear Algebra, MIT 18.06 (Strang), emphasis on eigenvalues, orthogonality, complex vector spaces, Hermitian matrices, diagonalisation.
2. Oscillations and waves (15 h): MIT 8.03 selected lectures, OpenStax Vol. 1 ch. 15 and Vol. 1 or 2 wave chapters.
3. Complex numbers (20 h): Khan Academy, MIT 18.04 early lectures, Beck et al. free text.
4. Ordinary differential equations (30 h): MIT 18.03SC, 3Blue1Brown differential equations series.
5. Electromagnetism (60 h): MIT 8.02 (Lewin), Feynman Lectures Vol. II, Tong's Electromagnetism.
6. Fourier analysis and PDEs (35 h): Steve Brunton, 18.03SC late units, 3Blue1Brown Fourier video.
7. Probability and special functions (20 h): Khan, MIT 18.05 selected.
8. Thermal and statistical physics (30 h): Susskind Statistical Mechanics, Tong, Feynman Vol. I.
9. Lagrangian and Hamiltonian mechanics (45 h): Susskind Classical Mechanics, Tong Classical Dynamics.
10. Special relativity (35 h), Old quantum theory (20 h), Quantum mechanics (125 h), Tensor calculus (40 h), General relativity and cosmology (90 h), History and primary sources (10 h): see `roadmap.md` for resources.
Gates (6 h each) and the capstone (25 h) do not need lesson lists beyond a test description.

## Authoring checklist
1. Read the module's hours and resource hints from `T` in the app file and `roadmap.md`.
2. Draft lessons in learning order; make hours add up; check that each prerequisite appears earlier.
3. Verify any resource you are not sure about by searching (course unit names, episode numbers and chapter numbers are easy to misremember).
4. Install: add the module to `LS` in `assets/frontierpath.html` using a targeted replacement; keep strings in double quotes and avoid double quotes inside text.
5. Republish the same file to the learner's existing page.
6. Tell the learner which modules still lack syllabi.
