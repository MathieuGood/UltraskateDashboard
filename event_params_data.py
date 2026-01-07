from models.event_params import EventParams
from models.track import Track
from webscraper.jms_site_params import JmsSiteParams
from webscraper.myraceresult_params import MyRaceResultParams

homestead_track = Track(
    name="Homestead Speedway", city="Homestead", country="USA", length_miles=1.46
)

miami_event_params: dict[int, EventParams] = {
    2013: EventParams(
        date="2013-01-07",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url="https://jms.racetecresults.com/results.aspx?CId=16370&RId=13",
            categories_indexes=[1],
            position_col_index=0,
            name_col_index=2,
        ),
    ),
    2014: EventParams(
        date="2014-01-20",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url="https://jms.racetecresults.com/results.aspx?CId=16370&RId=121",
            categories_indexes=[1, 2, 3, 4],
            position_col_index=0,
            name_col_index=2,
        ),
    ),
    2015: EventParams(
        date="2015-02-12",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url="https://jms.racetecresults.com/results.aspx?CId=16370&RId=179",
            categories_indexes=[1, 2, 3, 4],
            position_col_index=0,
            name_col_index=1,
        ),
    ),
    2016: EventParams(
        date="2016-02-26",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url="https://jms.racetecresults.com/results.aspx?CId=16370&RId=240",
            categories_indexes=[1, 3, 4],
            position_col_index=0,
            name_col_index=2,
        ),
    ),
    2017: EventParams(
        date="2017-01-16",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url="https://jms.racetecresults.com/results.aspx?CId=16370&RId=294",
            categories_indexes=[1, 3, 4],
            position_col_index=1,
            name_col_index=3,
        ),
    ),
    2018: EventParams(
        date="2018-01-10",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url="https://jms.racetecresults.com/results.aspx?CId=16370&RId=352",
            categories_indexes=[1, 2, 3, 4],
            position_col_index=1,
            name_col_index=3,
        ),
    ),
    2019: EventParams(
        date="2019-01-18",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url="https://jms.racetecresults.com/results.aspx?CId=16370&RId=352",
            categories_indexes=[1, 2, 3, 4],
            position_col_index=1,
            name_col_index=3,
        ),
    ),
    2020: EventParams(
        date="2020-01-17",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url="https://jms.racetecresults.com/results.aspx?CId=16370&RId=400",
            categories_indexes=[1, 2, 3, 4, 5],
            position_col_index=1,
            name_col_index=3,
        ),
    ),
    2021: EventParams(
        date="2021-01-29",
        track=homestead_track,
        scraped_site_params=JmsSiteParams(
            ranking_url="https://jms.racetecresults.com/results.aspx?CId=16370&RId=413",
            categories_indexes=[1, 3, 5],
            position_col_index=1,
            name_col_index=4,
            athlete_link_col_index=2,
        ),
    ),
    2022: EventParams(
        date="2022-02-19",
        track=homestead_track,
        scraped_site_params=MyRaceResultParams(race_id=192607),
    ),
    2023: EventParams(
        date="2023-02-10",
        track=homestead_track,
        scraped_site_params=MyRaceResultParams(race_id=204047),
    ),
    2024: EventParams(
        date="2024-02-15",
        track=homestead_track,
        scraped_site_params=MyRaceResultParams(race_id=259072),
    ),
    2025: EventParams(
        date="2025-02-25",
        track=homestead_track,
        scraped_site_params=MyRaceResultParams(race_id=310199),
    ),
}
