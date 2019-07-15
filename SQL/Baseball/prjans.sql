Select Position, AVG(Salary) as AvgSal
From baseball
group by Position
order by AvgSal desc