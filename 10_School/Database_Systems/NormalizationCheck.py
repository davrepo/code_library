# # Template
# def PrintSQL(Att1, Att2)
#     print ("Here make the SQL query to check %s --> %s" % (Att1, Att2));
#     print ("Use the query in Slide 44 of the Normalization lecture");

# # Python skeleton code to check all FDs of a relation R(A,B,C) with three attributes in step(a)
# R = ['A', 'B', 'C']
# for i in range(len(R)):
#     for j in range(len(R)):
#         if (i != j):
#             PrintSQL(R[i], R[j])
            
            
SQLquery = """
SELECT 'Person: %s --> %s' AS FD,
CASE WHEN COUNT(*)=0 THEN 'MAY HOLD'
ELSE 'does not hold' END AS VALIDITY
FROM (
    SELECT P.%s
    FROM Person P
    GROUP BY P.%s
    HAVING COUNT(DISTINCT P.%s) > 1
) X;
"""

def PrintSQL(Att1, Att2):
    print(SQLquery % (Att1, Att2, Att1, Att1, Att2));

R = ['id', 'name', 'zip', 'city']
for i in range(len(R)):
    for j in range(len(R)):
        if (i != j):
            PrintSQL(R[i], R[j])