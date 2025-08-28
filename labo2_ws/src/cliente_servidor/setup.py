from setuptools import find_packages, setup

package_name = 'cliente_servidor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nath',
    maintainer_email='nathalyarias897@gmail.com',
    description='Ejemplo cliente-servidor (AddTwoInts)',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'servidor_suma = cliente_servidor.servidor_suma:main', 'cliente_suma = cliente_servidor.cliente_suma:main',
        ],
    },
)
