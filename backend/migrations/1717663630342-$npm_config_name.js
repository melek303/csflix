import typeorm from "typeorm";

const { MigrationInterface, QueryRunner } = typeorm;

export default class  $npmConfigName1717663630342 {
    name = ' $npmConfigName1717663630342'

    async up(queryRunner) {
        await queryRunner.query(`
            CREATE TABLE "temporary_movie" (
                "id" integer PRIMARY KEY NOT NULL,
                "original_title" varchar NOT NULL,
                "release_date" varchar NOT NULL,
                "backdrop_path" varchar NOT NULL,
                "original_language" varchar NOT NULL,
                "genre_ids" varchar NOT NULL,
                CONSTRAINT "UQ_cb3bb4d61cf764dc035cbedd422" UNIQUE ("id")
            )
        `);
        await queryRunner.query(`
            INSERT INTO "temporary_movie"(
                    "id",
                    "original_title",
                    "release_date",
                    "backdrop_path",
                    "original_language",
                    "genre_ids"
                )
            SELECT "id",
                "original_title",
                "release_date",
                "backdrop_path",
                "original_language",
                "genre_ids"
            FROM "movie"
        `);
        await queryRunner.query(`
            DROP TABLE "movie"
        `);
        await queryRunner.query(`
            ALTER TABLE "temporary_movie"
                RENAME TO "movie"
        `);
        await queryRunner.query(`
            CREATE TABLE "temporary_movie" (
                "id" integer PRIMARY KEY NOT NULL,
                "original_title" varchar NOT NULL,
                "release_date" varchar NOT NULL,
                "backdrop_path" varchar NOT NULL,
                "original_language" varchar NOT NULL,
                "genre_ids" varchar NOT NULL,
                "adult" boolean NOT NULL,
                CONSTRAINT "UQ_cb3bb4d61cf764dc035cbedd422" UNIQUE ("id")
            )
        `);
        await queryRunner.query(`
            INSERT INTO "temporary_movie"(
                    "id",
                    "original_title",
                    "release_date",
                    "backdrop_path",
                    "original_language",
                    "genre_ids"
                )
            SELECT "id",
                "original_title",
                "release_date",
                "backdrop_path",
                "original_language",
                "genre_ids"
            FROM "movie"
        `);
        await queryRunner.query(`
            DROP TABLE "movie"
        `);
        await queryRunner.query(`
            ALTER TABLE "temporary_movie"
                RENAME TO "movie"
        `);
        await queryRunner.query(`
            CREATE TABLE "temporary_movie" (
                "id" integer PRIMARY KEY NOT NULL,
                "original_title" varchar NOT NULL,
                "release_date" varchar NOT NULL,
                "backdrop_path" varchar NOT NULL,
                "original_language" varchar NOT NULL,
                "genre_ids" text NOT NULL,
                "adult" boolean NOT NULL,
                CONSTRAINT "UQ_cb3bb4d61cf764dc035cbedd422" UNIQUE ("id")
            )
        `);
        await queryRunner.query(`
            INSERT INTO "temporary_movie"(
                    "id",
                    "original_title",
                    "release_date",
                    "backdrop_path",
                    "original_language",
                    "genre_ids",
                    "adult"
                )
            SELECT "id",
                "original_title",
                "release_date",
                "backdrop_path",
                "original_language",
                "genre_ids",
                "adult"
            FROM "movie"
        `);
        await queryRunner.query(`
            DROP TABLE "movie"
        `);
        await queryRunner.query(`
            ALTER TABLE "temporary_movie"
                RENAME TO "movie"
        `);
    }

    async down(queryRunner) {
        await queryRunner.query(`
            ALTER TABLE "movie"
                RENAME TO "temporary_movie"
        `);
        await queryRunner.query(`
            CREATE TABLE "movie" (
                "id" integer PRIMARY KEY NOT NULL,
                "original_title" varchar NOT NULL,
                "release_date" varchar NOT NULL,
                "backdrop_path" varchar NOT NULL,
                "original_language" varchar NOT NULL,
                "genre_ids" varchar NOT NULL,
                "adult" boolean NOT NULL,
                CONSTRAINT "UQ_cb3bb4d61cf764dc035cbedd422" UNIQUE ("id")
            )
        `);
        await queryRunner.query(`
            INSERT INTO "movie"(
                    "id",
                    "original_title",
                    "release_date",
                    "backdrop_path",
                    "original_language",
                    "genre_ids",
                    "adult"
                )
            SELECT "id",
                "original_title",
                "release_date",
                "backdrop_path",
                "original_language",
                "genre_ids",
                "adult"
            FROM "temporary_movie"
        `);
        await queryRunner.query(`
            DROP TABLE "temporary_movie"
        `);
        await queryRunner.query(`
            ALTER TABLE "movie"
                RENAME TO "temporary_movie"
        `);
        await queryRunner.query(`
            CREATE TABLE "movie" (
                "id" integer PRIMARY KEY NOT NULL,
                "original_title" varchar NOT NULL,
                "release_date" varchar NOT NULL,
                "backdrop_path" varchar NOT NULL,
                "original_language" varchar NOT NULL,
                "genre_ids" varchar NOT NULL,
                CONSTRAINT "UQ_cb3bb4d61cf764dc035cbedd422" UNIQUE ("id")
            )
        `);
        await queryRunner.query(`
            INSERT INTO "movie"(
                    "id",
                    "original_title",
                    "release_date",
                    "backdrop_path",
                    "original_language",
                    "genre_ids"
                )
            SELECT "id",
                "original_title",
                "release_date",
                "backdrop_path",
                "original_language",
                "genre_ids"
            FROM "temporary_movie"
        `);
        await queryRunner.query(`
            DROP TABLE "temporary_movie"
        `);
        await queryRunner.query(`
            ALTER TABLE "movie"
                RENAME TO "temporary_movie"
        `);
        await queryRunner.query(`
            CREATE TABLE "movie" (
                "id" integer PRIMARY KEY NOT NULL,
                "original_title" varchar NOT NULL,
                "release_date" varchar NOT NULL,
                "backdrop_path" varchar NOT NULL,
                "original_language" varchar NOT NULL,
                "genre_ids" varchar NOT NULL,
                "key" varchar NOT NULL,
                CONSTRAINT "UQ_cb3bb4d61cf764dc035cbedd422" UNIQUE ("id")
            )
        `);
        await queryRunner.query(`
            INSERT INTO "movie"(
                    "id",
                    "original_title",
                    "release_date",
                    "backdrop_path",
                    "original_language",
                    "genre_ids"
                )
            SELECT "id",
                "original_title",
                "release_date",
                "backdrop_path",
                "original_language",
                "genre_ids"
            FROM "temporary_movie"
        `);
        await queryRunner.query(`
            DROP TABLE "temporary_movie"
        `);
    }
}
