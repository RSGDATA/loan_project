CREATE TABLE lending_club_rejected_klean
(
"Amount Requested" float8,
"Application Date" date,
"Loan Title" VARCHAR(255),
"Risk_Score" float8,
"Debt-To-Income Ratio" float8,
"State" VARCHAR(5),
"Employment Length" float8,
"Policy Code" float8
);

SELECT "Loan Title" FROM lending_club_rejected_klean
WHERE "Loan Title" LIKE 