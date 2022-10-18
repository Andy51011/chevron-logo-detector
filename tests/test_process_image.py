from process_image import ProcessImage


def test_if_is_empty_processed_img_dict() -> None:
    process_image = ProcessImage()
    process_item_dict = process_image.processed_img_dict
    assert bool(process_item_dict) is False


def test_is_not_empty_processed_img_dict() -> None:
    process_image = ProcessImage()
    process_item_dict = process_image.processed_img_dict["test"] = ["logo"]
    assert bool(process_item_dict) is True


def test_dict_value_should_be_dict() -> None:
    process_image = ProcessImage()
    process_item_dict = process_image.processed_img_dict
    assert type(process_item_dict) is dict


def test_initial_directory_is_null() -> None:
    process_image = ProcessImage()
    assert process_image.directory is None


def test_directory_is_string() -> None:
    process_image = ProcessImage()
    directory = process_image.directory = "/test/directory/"
    assert type(directory) is str


def test_directory_not_string() -> None:
    process_image = ProcessImage()
    directory = process_image.directory = 1123
    assert not str(directory) is True


def test_filter_img(tmpdir) -> None:
    process_image = ProcessImage()
    process_image.directory = "mydirectory"
    process_image.processed_img_dict["test"] = [{"description": "logo"}]
    print(process_image.processed_img_dict.items())
    for file, logos in process_image.processed_img_dict.items():
        temporary_path = tmpdir.mkdir(process_image.directory).join(file)
        print(logos)
        if not logos:
            process_image.failed_image_count += 1
        elif logos[0]["description"] == "logo":
            process_image.chevron_logo_image_count += 1
        else:
            process_image.undetected_logo_image_count += 1
    assert process_image.chevron_logo_image_count == 1
