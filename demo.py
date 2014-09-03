from flask import Flask, render_template, redirect, url_for, request
from flask import make_response


app = Flask(__name__)
app.debug = True


SHIB_KEYS = [
    'AUTH_TYPE',
    'HTTP_COOKIE',
    'persistent-id',
    'affiliation',
    'REMOTE_USER',
    'entitlement',
    'Shib-AuthnContext-Class',
    'Shib-Authentication-Method',
    'Shib-Authentication-Instant',
    'Shib-Session-Index',
    'Shib-Application-ID',
    'eppn',
    'Shib-Identity-Provider',
    'Shib-Session-ID',
]


class login_required(object):
    def __init__(self, view):
        self.view = view
        self.__name__ = view.__name__

    def __call__(self, *args, **kwargs):
        if not self.is_authenticated():
            return redirect(url_for('login') + '?next=' + request.path)
        return self.view(*args, **kwargs)

    def is_authenticated(self):
        if request.environ.get('AUTH_TYPE', None) == 'shibboleth':
            if request.environ.get('REMOTE_USER', None):
                return True
        return False


@app.context_processor
def get_user():
    user = None
    if request.environ.get('AUTH_TYPE', None) == 'shibboleth':
        user = request.environ.get('REMOTE_USER', None)
    return {
        'user': user
    }


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/')
def login():
    return redirect('/Shibboleth.sso/Login?target={}'.format(
        request.args.get('next', '/')))


@app.route('/logout/')
def logout():
    resp = make_response(redirect(request.args.get('next', '/')))

    for c in request.cookies:
        if c.startswith('_shibsession_'):
            resp.set_cookie(c, '', expires=0)

    return resp


@app.route('/protected/')
@login_required
def protected():
    return render_template('secure.html', env=request.environ, keys=SHIB_KEYS)


@app.route('/public/')
def public():
    return render_template('public.html', env=request.environ, keys=SHIB_KEYS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4900)
