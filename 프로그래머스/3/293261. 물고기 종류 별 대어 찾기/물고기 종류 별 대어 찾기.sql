# select
#     fish_info.id,
#     fish_name_info.fish_name,
#     max(fish_info.length) as length
# from fish_info
# join fish_name_info 
#     on fish_name_info.fish_type = fish_info.fish_type
# group by fish_name_info.fish_name
# order by fish_info.id ASC

SELECT
    i.id,
    n.fish_name,
    i.length
FROM fish_info i
JOIN fish_name_info n
    ON n.fish_type = i.fish_type
WHERE i.length = (
    SELECT MAX(subi.length)
    FROM fish_info subi
    WHERE subi.fish_type = i.fish_type
)
ORDER BY i.id ASC;


# select
# *
# from fish_info

# select
# *
# from fish_name_info