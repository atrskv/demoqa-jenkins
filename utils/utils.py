from selene.support.shared import browser


def delete_interrupt_elements():

    browser.driver.execute_script('''
    document.querySelector('.Advertisement-Section')
    .remove()
    '''
    )


def resource(path):
    import demoqa_tests
    from pathlib import Path
    return str(
        Path(demoqa_tests.__file__)
        .parent
        .parent
        .joinpath(f'resources/{path}')
    )