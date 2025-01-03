select
   id,
   case
   when SIZE_OF_COLONY <= 100 then 'LOW'
   when 100 < SIZE_OF_COLONY AND SIZE_OF_COLONY <= 1000 then 'MEDIUM'
   when SIZE_OF_COLONY > 1000 then 'HIGH'
   end
   as size
from
    ecoli_data
order by id ASC
