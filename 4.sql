CREATE TABLE "game_df8" (
  "game_id" SERIAL PRIMARY KEY,
  "title" varchar(255),
  "release_date" date,
  "rating" varchar(255),
  "description" varchar(10000),
  "score" integer,
  "genre" varchar(255),
  "created_at" timestamp
);

select * FROM game_df8;

CREATE TABLE "platform_df8" (
  "platform_id" SERIAL PRIMARY KEY,
  "platform" varchar(255),
  "created_at" timestamp
);

CREATE TABLE "publisher_df8" (
  "publisher_id" SERIAL PRIMARY KEY,
  "publisher" varchar(255),
  "created_at" timestamp
);

CREATE TABLE "sale_df8" (
  "sale_id" SERIAL PRIMARY KEY,
  "game_id" integer REFERENCES game_df8(game_id),
  "platform_id" integer REFERENCES platform_df8(platform_id),
  "publisher_id" integer REFERENCES publisher_df8(publisher_id),
  "NA_Sales" float,
  "EU_Sales" float,
  "JP_Sales" float,
  "Other_Sales" float,
  "Global_Sales" float,
  "created_at" timestamp
);

ALTER TABLE "sale_df8" ADD FOREIGN KEY ("game_id") REFERENCES "game_df8" ("game_id");

ALTER TABLE "sale_df8" ADD FOREIGN KEY ("platform_id") REFERENCES "platform_df8" ("platform_id");

ALTER TABLE "sale_df8" ADD FOREIGN KEY ("publisher_id") REFERENCES "publisher_df8" ("publisher_id");
