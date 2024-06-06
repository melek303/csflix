import typeorm from "typeorm";

const { MigrationInterface, QueryRunner } = typeorm;

export default class  $npmConfigName1717624335767 {
    name = ' $npmConfigName1717624335767'

    async up(queryRunner) {
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
    }

    async down(queryRunner) {
        await queryRunner.query(`
            DROP TABLE "movie"
        `);
    }
}
