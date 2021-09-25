CREATE TABLE IF NOT EXISTS request_json_retrieval_example (
	id int8 NULL,
	"utcDate" text NULL,
	status text NULL,
	matchday int8 NULL,
	stage text NULL,
	"group" text NULL,
	"lastUpdated" text NULL,
	season_id int8 NULL,
	"season_startDate" text NULL,
	"season_endDate" text NULL,
	"season_currentMatchday" int8 NULL,
	"odds_homeWin" float8 NULL,
	odds_draw float8 NULL,
	"odds_awayWin" float8 NULL,
	score_winner text NULL,
	score_duration text NULL,
	"score_fullTime_homeTeam" float8 NULL,
	"score_fullTime_awayTeam" float8 NULL,
	"score_halfTime_homeTeam" float8 NULL,
	"score_halfTime_awayTeam" float8 NULL,
	"score_extraTime_homeTeam" text NULL,
	"score_extraTime_awayTeam" text NULL,
	"score_penalties_homeTeam" text NULL,
	"score_penalties_awayTeam" text NULL,
	"homeTeam_id" int8 NULL,
	"homeTeam_name" text NULL,
	"awayTeam_id" int8 NULL,
	"awayTeam_name" text NULL
);




CREATE TABLE IF NOT EXISTS parquet_data_example (
	idx_id int8 NULL,
	marketplace text NULL,
	customer_id int8 NULL,
	review_id text NULL,
	product_id text NULL,
	product_parent int8 NULL,
	product_title text NULL,
	star_rating int8 NULL,
	helpful_votes int8 NULL,
	total_votes int8 NULL,
	vine text NULL,
	verified_purchase text NULL,
	review_headline text NULL,
	review_body text NULL,
	review_date text NULL,
	"year" int8 NULL
);


CREATE TABLE IF NOT EXISTS fixed_width_data_example (
	id text NULL,
	latitude float8 NULL,
	longitude float8 NULL,
	elevation float8 NULL,
	state text NULL,
	"name" text NULL,
	"gsn flag" text NULL,
	hcn_crn_flag text NULL,
	wmo_id float8 NULL
);


CREATE TABLE IF NOT EXISTS variable_length_data_example (
	"Grade" text NULL,
	"Year" int8 NULL,
	"Category" text NULL,
	"Number Tested" int8 NULL,
	"Mean Scale Score" int8 NULL,
	"Level 1 #" int8 NULL,
	"Level 1 %" float8 NULL,
	"Level 2 #" int8 NULL,
	"Level 2 %" float8 NULL,
	"Level 3 #" int8 NULL,
	"Level 3 %" float8 NULL,
	"Level 4 #" int8 NULL,
	"Level 4 %" float8 NULL,
	"Level 3+4 #" int8 NULL,
	"Level 3+4 %" float8 NULL
);