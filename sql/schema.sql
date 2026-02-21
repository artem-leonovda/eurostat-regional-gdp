DROP TABLE IF EXISTS regional_gdp;

CREATE TABLE IF NOT EXISTS regional_gdp (
    geo_code TEXT NOT NULL,
    year INT NOT NULL,
    gdp_mio_eur NUMERIC NOT NULL,
    PRIMARY KEY (geo_code, year)
);

CREATE INDEX IF NOT EXISTS idx_regional_gdp_year ON regional_gdp(year);
CREATE INDEX IF NOT EXISTS idx_regional_gdp_geo ON regional_gdp(geo_code);
