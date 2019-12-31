from orator.migrations import Migration


class CreateArticlesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('articles') as table:
            table.increments('id')
            table.string('domain', 255)
            table.string('url')
            table.string('title')
            table.string('main_text')
            table.datetime('published_at').nullable()
            table.integer('hatena_bookmark_count').unsigned()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('articles')