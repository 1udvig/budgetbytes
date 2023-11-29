import click
from datetime import datetime


def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return None


@click.group()
def cli():
    pass


@click.command()
def add_transaction():
    date = None
    while date is None:
        date_str = click.prompt(
            'Enter the date of the transaction (YYYY-MM-DD)', type=str)
        date = validate_date(date_str)
        if date is None:
            click.echo("Invalid date format. Please use YYYY-MM-DD.")

    amount = click.prompt('Enter the transaction amount', type=float)
    description = click.prompt(
        'Enter a description for the transaction', type=str)
    transaction_type = click.prompt(
        'Enter the transaction type',
        type=click.Choice(['income', 'expense'], case_sensitive=False)
    )

    # Process the transaction...
    click.echo(
        f"Added: Date: {date.strftime('%Y-%m-%d')}, Amount: {amount}, Description: '{description}', Type: {transaction_type}")


def save_transaction(date, amount, description, transaction_type):
    click.echo(
        f"Added the following transaction to the database: Date: {date}, Amount: {amount}, Description: '{description}', Type: {transaction_type}")

    pass


@click.command()
def generate_balance_sheet():
    # Logic to generate a balance sheet
    pass


@click.command()
def generate_results():
    # Logic to generate annual results
    pass


cli.add_command(add_transaction)
cli.add_command(generate_balance_sheet)
cli.add_command(generate_results)

if __name__ == '__main__':
    cli()
