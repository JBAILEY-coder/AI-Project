:- discontiguous GradePoint/3.
:- discontiguous gradePoint/3.
:- discontiguous cumulative/5.
:- discontiguous sumCredits/2.

default_gpa(2.2)

% gradePoint(grade, credit) takes grade and credit for a course, return gpa for that course
% gradePoint(grade, credit, gpa) takes grade and credit for a course, calculates and returns gpa for that course
gradePoint(Grade, Credit, GPA) :-
    gradePoint(Grade, GradePoint),  % Look up the grade point for the given letter grade
    GPA is GradePoint * Credit.

% gradePointEarned([gradePoints], [totalCredits]) takes a list of gradepoints for a student and total credits, return gpa
calGpa(GradePoints, Credits, GPA) :-
    sum_list(GradePoints, TotalGradePoints),
    sum_list(Credits, TotalCredits),
    GPA is TotalGradePoints / TotalCredits.

% cumulative(gpaSem1, gpaSem2, totalCreditsSem1, totalCreditsSem2) return cumulative gpa
cumulative(GPASem1, GPASem2, TotalCreditsSem1, TotalCreditsSem2, CumulativeGPA) :-
    TotalCredits is TotalCreditsSem1 + TotalCreditsSem2,
    GPASem1Credits is GPASem1 * TotalCreditsSem1,
    GPASem2Credits is GPASem2 * TotalCreditsSem2,
    CumulativeGPA is (GPASem1Credits + GPASem2Credits) / TotalCredits.

% sumCredits([creditList]) returns a sum of all credits.
sumCredits(CreditList, TotalCredits) :-
    sum_list(CreditList, TotalCredits).




%Examples usage below:

% Calculate GPA for a single course with 3 credits and grade 'B':
%?- gradePoint('B', 3, GPA).

% Calculate GPA for a single course with 4 credits and grade 'A+':
%?- gradePoint('A+', 4, GPA).

% Calculate GPA for a list of grade points (e.g., [3.0, 2.7, 4.0]) with a total of 12 credits:
%?- gradePointEarned([3.0, 2.7, 4.0], 12, GPA).

% Calculate cumulative GPA for two semesters with the following details:
% - Semester 1: GPA = 3.5, Total Credits = 15
% - Semester 2: GPA = 3.2, Total Credits = 18
%?- cumulative(3.5, 3.2, 15, 18, CumulativeGPA).

% Calculate the sum of credits for a list of credits (e.g., [3, 4, 3, 2]):
%?- sumCredits([3, 4, 3, 2], TotalCredits).
