"""
Sentry
"""
import sentry_sdk

from sec_ingress import util


def configure_sentry():
    """
    Sets up Sentry
    """
    sentry_sdk.init(
        dsn=util.get_env_var("SENTRY_DNS"),
        traces_sample_rate=1,
        send_default_pii=True,
        debug=False,
        environment=util.get_env_var("ENVIRONMENT"),
    )
