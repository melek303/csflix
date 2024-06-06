import typeorm from "typeorm";

const { MigrationInterface, QueryRunner } = typeorm;

export default class  $npmConfigName1717665762823 {
    name = ' $npmConfigName1717665762823'

    async up(queryRunner) {
        await queryRunner.query(`
            CREATE TABLE "temporary_user" (
                "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                "email" varchar NOT NULL,
                "firstname" varchar NOT NULL,
                "lastname" varchar NOT NULL,
                "liked_movies" text,
                "adult" boolean NOT NULL,
                CONSTRAINT "UQ_e12875dfb3b1d92d7d7c5377e22" UNIQUE ("email")
            )
        `);
        await queryRunner.query(`
            INSERT INTO "temporary_user"("id", "email", "firstname", "lastname")
            SELECT "id",
                "email",
                "firstname",
                "lastname"
            FROM "user"
        `);
        await queryRunner.query(`
            DROP TABLE "user"
        `);
        await queryRunner.query(`
            ALTER TABLE "temporary_user"
                RENAME TO "user"
        `);
    }

    async down(queryRunner) {
        await queryRunner.query(`
            ALTER TABLE "user"
                RENAME TO "temporary_user"
        `);
        await queryRunner.query(`
            CREATE TABLE "user" (
                "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
                "email" varchar NOT NULL,
                "firstname" varchar NOT NULL,
                "lastname" varchar NOT NULL,
                CONSTRAINT "UQ_e12875dfb3b1d92d7d7c5377e22" UNIQUE ("email")
            )
        `);
        await queryRunner.query(`
            INSERT INTO "user"("id", "email", "firstname", "lastname")
            SELECT "id",
                "email",
                "firstname",
                "lastname"
            FROM "temporary_user"
        `);
        await queryRunner.query(`
            DROP TABLE "temporary_user"
        `);
    }
}
