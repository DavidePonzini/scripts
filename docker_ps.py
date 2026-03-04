#!/usr/bin/env python

import docker
from docker.models.containers import Container
from dav_tools import messages

PADDINGS = [13, 20, 30, 20, 20]

def print_header():
    messages.message(
        'CONTAINER ID', 'IMAGE', 'CREATED', 'STATUS', 'NAME',
        text_min_len=PADDINGS,
        default_text_options=[
            messages.TextFormat.Style.BOLD,
            messages.TextFormat.Color.GREEN,
        ],
    )

    messages.message(
        '=' * 150,
        default_text_options=[
            messages.TextFormat.Style.BOLD,
            messages.TextFormat.Color.GREEN,
        ],
    )


def print_container_stats(container_id: str, image: str, created: str, status: str, ports: dict[str, list[dict[str, str]]], name: str):
    messages.message(
        container_id, image, created, status, name,
        text_min_len=PADDINGS,
        default_text_options=[
            messages.TextFormat.Style.BOLD,
            messages.TextFormat.Color.YELLOW,
        ],
    )


    for port, mappings in ports.items():
        # Port is not exposed
        if mappings is None:
            messages.message(
                f'    {port}',
                default_text_options=[
                    messages.TextFormat.Color.BLUE,
                ],
            )
            continue

        # Port is exposed
        for mapping in mappings:
            host_port = mapping.get('HostPort')
            host_ip = mapping.get('HostIp')
            if host_ip == '::':
                host_ip = '[::]'

            messages.message(
                f'    {host_ip}:{host_port} -> {port}',
                default_text_options=[
                    messages.TextFormat.Color.BLUE,
                ],
            )





if __name__ == '__main__':
    client = docker.from_env()
    containers = client.containers.list()

    if not containers:
        messages.info("No running containers found.")
    else:
        print_header()
        for container in containers:
            image = container.image
            if image is not None:
                image = image.tags[0].split(':')[0] if image.tags else image.short_id
            else:
                image = 'Unknown'

            name = container.name
            if name is None:
                name = 'Unknown'

            print_container_stats(
                container_id=container.short_id,
                image=image,
                created=container.attrs['Created'],
                status=container.status,
                ports=container.attrs['NetworkSettings']['Ports'],
                name=name,
            )
