class AndLocators(object):

    #POPUP ALERT LOCATORS
    LOC_ENVIRONMENT_LIST_POPUP_HEADER = "//android.widget.TextView[@resource-id='com.reviverauto.rplate:id/alertTitle']"
    LOC_ENVIRONMENT_STAGING = "//android.widget.TextView[@resource-id='android:id/text1' and  @index='0']"
    LOC_ENVIRONMENT_QA = "//android.widget.TextView[@resource-id='android:id/text1' and  @index='1']"
    LOC_ENVIRONMENT_PRODUCTION = "//android.widget.TextView[@resource-id='android:id/text1' and  @index='2']"
    LOC_ENVIRONMENT_PILOT = "//android.widget.TextView[@resource-id='android:id/text1' and  @index='3']"
    LOC_ENVIRONMENT_DUBAI = "//android.widget.TextView[@resource-id='android:id/text1' and  @index='4']"
    LOC_ENVIRONMENT_PRE_PRODUCTION = "//android.widget.TextView[@resource-id='android:id/text1' and  @index='5']"

    #SPLASH SCREEN LOCATORS
    LOC_LOGO_IMAGE_SPLASHSCREEN = "//android.widget.ImageView[@resource-id='com.reviverauto.rplate:id/image_splash' and  @index='0']"
    LOC_LOGO_SUBTITLE = "//android.widget.TextView[@resource-id='com.reviverauto.rplate:id/txt_manage_track_customize' and  @index='1']"
    LOC_SIGNIN = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]"
    LOC_SIGNUP = "//android.widget.TextView[@resource-id='com.reviverauto.rplate:id/txtSignUp' and  @index='1']"
    BOUNDS_SIGNIN={'x':200,'y':1670}

    #LOGIN PAGE LOCATORS
    LOC_NAVIGATOR_HEADER = "//android.widget.ImageButton[@content-desc='Navigate up' and  @index='0']"
    LOC_SIGNUP_TITLE = "//android.view.ViewGroup[@resource-id='com.reviverauto.rplate:id/action_bar']/android.widget.TextView[@index'1']"
    LOC_EMAIL_TEXTBOX = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/TextInputLayout/android.widget.FrameLayout/android.widget.EditText"
    LOC_EMAIL_IMAGE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.ImageView"
    LOC_EMAIL_ERROR="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/TextInputLayout/android.widget.LinearLayout/android.widget.TextView"
    LOC_PASSWORD_TEXTBOX = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/TextInputLayout/android.widget.FrameLayout/android.widget.EditText"
    LOC_PASSWORD_IMAGE = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.ImageView"
    LOC_PASSWORD_TOGLER = "//android.widget.ImageButton[@content-desc='Toggle password visibility']"
    LOC_SIGNIN_BUTTON = "//android.widget.Button[@resource-id='com.reviverauto.rplate:id/btn_sign_in' and  @index='2']"
    LOC_FORGOTPASSWORD_LINK="//android.widget.TextView[@resource-id='com.reviverauto.rplate:id/txt_signin_forgot_password' and  @index='3']"
    LOC_PASSWORD_ERROR = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/TextInputLayout/android.widget.LinearLayout/android.widget.TextView"

    #FORGOT PASSWORD PAGE
    LOC_FP_NAVIGATOR="//android.widget.ImageButton[@content-desc='Navigate up']"
    LOC_FP_TITLE="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView"
    LOC_FP_TEXT="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView"
    LOC_FP_TEXTBOX="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/TextInputLayout/android.widget.FrameLayout/android.widget.EditText"
    LOC_FB_IMAGE="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView"
    LOC_SEND_BUTTON="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button"
    LOC_FB_BOTTOMTEXT="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]"
    LOC_FP_LINK="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[2]"
    LOC_FP_ERROR="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/TextInputLayout/android.widget.LinearLayout/android.widget.TextView"
    LOC_FP_SUCCESS_POPUP_HEAD="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView"
    LOC_FP_SUCCESS_POPUP_TEXT="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView"
    LOC_FP_OK_ONPOPUP="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.Button"

    #SIGNUP PAGE
    LOC_SUP_NAVIGATOR="//android.widget.ImageButton[@content-desc='Navigate up']"
    LOC_SUP_TITLE="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView"

    #HOMEPAGE
    LOC_HOMEPAGE_TOOLBAR="//android.view.ViewGroup[@resource-id='com.reviverauto.rplate:id/toolbar' and @index='0']"
    LOC_HOMEPAGE_BURGER_ICON="//android.widget.ImageButton[@content-desc='Navigate up' and @index='0']"
    BOUNDS_BURGERICON={'x':30,'y':160}
    LOC_HOMEPAGE_RPLATELAYOUT="//android.widget.RelativeLayout[@resource-id='com.reviverauto.rplate:id/toolbar' and @index='0']"
    LOC_HOMEPAGE_DEVICEPOPUP_ALLOW="//android.widget.Button[@resource-id='com.android.packageinstaller:id/permission_allow_button' and @index='1']"
    LOC_HOMEPAGE_DEVICEPOPUP_DENY = "//android.widget.Button[@resource-id='com.android.packageinstaller:id/permission_deny_button' and @index='0']"

    #NAVIGATOR
    LOC_NAVIGATOR_USERNAME="//android.widget.TextView[@resource-id='com.reviverauto.rplate:id/txt_nav_email_id' and @index='2']"
    LOC_NM_ACCOUNTSETTINGS = "//android.widget.CheckedTextView[@resource-id='com.reviverauto.rplate:id/design_menu_item_text' and @index='0']"

    #ACCOUNT PAGE
    LOC_AP_SIGNOUTBUTTON="//android.widget.TextView[@resource-id='com.reviverauto.rplate:id/txt_sign_out' and @index='8' and @text='Sign Out']"
