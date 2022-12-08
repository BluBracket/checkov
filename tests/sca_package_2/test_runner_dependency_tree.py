from pathlib import Path
from packaging import version as packaging_version
from checkov.common.bridgecrew.severities import Severities, BcSeverities
from checkov.common.models.enums import CheckResult

EXAMPLES_DIR = Path(__file__).parent / "examples"


def test_run(sca_package_report_dt):
    # given
    report = sca_package_report_dt
    # then
    assert report.check_type == "sca_package"

    assert report.resources == {'package-lock.json.mocha', 'requirements.txt.pyyaml', 'package-lock.json.grunt',
                                'package-lock.json.nconf', 'requirements.txt.pyramid',
                                'package-files/yarn/package.json.bcrypt-nodejs', 'requirements.txt.gevent',
                                'requirements.txt.psycopg', 'requirements.txt.streamlit',
                                'package-files/yarn/package.json.node-esapi', 'package-lock.json.marked',
                                'package-lock.json.cypress',
                                'package-files/java/gradle/normal/build.gradle.commons-beanutils_commons-beanutils',
                                'requirements.txt.aiohttp',
                                'package-files/java/gradle/normal/build.gradle.org.apache.httpcomponents_httpclient',
                                'requirements.txt.yarl', 'requirements.txt.grpcio_tools',
                                'package-lock.json.unset-value',
                                'package-files/java/maven/normal/pom.xml.org.apache.logging.log4j_log4j-core',
                                'requirements.txt.pymysql', 'requirements.txt.contextvars',
                                'package-lock.json.minimist', 'requirements.txt.pika', 'requirements.txt.requests',
                                'requirements.txt.wrapt', 'package-files/yarn/package.json.marked',
                                'requirements.txt.werkzeug', 'requirements.txt.celery', 'requirements.txt.protobuf',
                                'package-lock.json.decode-uri-component', 'requirements.txt.flask',
                                'requirements.txt.uvicorn',
                                'package-files/java/maven/normal/pom.xml.commons-collections_commons-collections',
                                'requirements.txt.multidict', 'requirements.txt.elasticsearch',
                                'package-lock.json.helmet', 'package-files/java/maven/normal/pom.xml.junit_junit',
                                'requirements.txt.sanic', 'requirements.txt.mysqlclient',
                                'package-lock.json.glob-parent', 'requirements.txt.kafka-python',
                                'requirements.txt.tornado', 'requirements.txt.testcontainers',
                                'package-lock.json.helmet-csp',
                                'package-files/java/gradle/normal/build.gradle.com.fasterxml.jackson.core_jackson-databind',
                                'requirements.txt.hug', 'package-lock.json.debug', 'requirements.txt.pymongo',
                                'requirements.txt.fastapi', 'package-lock.json.mongodb', 'requirements.txt.packaging',
                                'requirements.txt.django', 'package-lock.json.bson', 'requirements.txt.redis',
                                'requirements.txt.urllib3', 'package-lock.json.uglify-js',
                                'package-files/yarn/package.json.needle', 'requirements.txt.gunicorn'}
    assert len(report.passed_checks) == 34
    assert len(report.failed_checks) == 67
    assert len(report.skipped_checks) == 0
    assert len(report.parsing_errors) == 0

    cve_record = next((c for c in report.failed_checks if
                       c.resource == "package-lock.json.bson"
                       and c.vulnerability_details.get('root_package_name', "") == 'mongodb'
                       and c.check_name == "SCA package scan"), None)
    assert cve_record is not None
    assert cve_record.bc_check_id == 'BC_CVE_2019_2391'
    assert cve_record.check_id == 'CKV_CVE_2019_2391'
    assert cve_record.check_class == "mock.mock.MagicMock"  # not the real one
    assert cve_record.check_name == "SCA package scan"
    assert cve_record.check_result == {"result": CheckResult.FAILED}
    assert cve_record.code_block == [(0, 'bson: 1.0.9')]
    assert cve_record.description == (
        'Incorrect parsing of certain JSON input may result in js-bson not correctly serializing BSON. '
        'This may cause unexpected application behaviour including data disclosure. '
        'This issue affects: MongoDB Inc. js-bson library version 1.1.3 and prior to.'
    )
    assert cve_record.file_abs_path == "/package-lock.json"
    assert cve_record.file_line_range == [0, 0]
    assert cve_record.file_path == "/package-lock.json"
    assert cve_record.repo_file_path == "/package-lock.json"
    assert cve_record.resource == 'package-lock.json.bson'
    assert cve_record.severity == Severities[BcSeverities.MEDIUM]
    assert cve_record.short_description == 'CVE-2019-2391 - bson: 1.0.9'
    assert cve_record.vulnerability_details["lowest_fixed_version"] == "1.1.4"
    assert cve_record.vulnerability_details["fixed_versions"] == [
        packaging_version.parse("1.1.4"),
    ]
    assert cve_record.vulnerability_details['root_package_name'] == 'mongodb'
    assert cve_record.vulnerability_details['root_package_version'] == '2.2.36'
    assert cve_record.vulnerability_details['root_package_fix_version'] == '3.1.13'
