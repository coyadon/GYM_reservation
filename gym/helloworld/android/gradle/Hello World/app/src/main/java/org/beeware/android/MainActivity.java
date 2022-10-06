package org.beeware.android;

import android.content.Intent;
import android.content.res.Configuration;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.LinearLayout;

import androidx.appcompat.app.AppCompatActivity;

import com.chaquo.python.Kwarg;
import com.chaquo.python.PyException;
import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

import com.example.helloworld.R;


public class MainActivity extends AppCompatActivity {

    // To profile app launch, use `adb -s MainActivity`; look for "onCreate() start" and "onResume() completed".
    private String TAG = "MainActivity";
    private static PyObject pythonApp;

    /**
     * This method is called by `app.__main__` over JNI in Python when the BeeWare
     * app launches.
     *
     * @param app
     */
    @SuppressWarnings("unused")
    public static void setPythonApp(IPythonApp app) {
        pythonApp = PyObject.fromJava(app);
    }

    /**
     * We store the MainActivity instance on the *class* so that we can easily
     * access it from Python.
     */
    public static MainActivity singletonThis;

    protected void onCreate(Bundle savedInstanceState) {
        Log.d(TAG, "onCreate() start");
        this.captureStdoutStderr();
        Log.d(TAG, "onCreate(): captured stdout/stderr");
        // Change away from the splash screen theme to the app theme.
        setTheme(R.style.AppTheme);
        super.onCreate(savedInstanceState);
        LinearLayout layout = new LinearLayout(this);
        this.setContentView(layout);
        singletonThis = this;

        if (Python.isStarted()) {
            Log.d(TAG, "Python already started");
        } else {
            Log.d(TAG, "Starting Python");
            Python.start(new AndroidPlatform(this));
        }
        Python py = Python.getInstance();
        Log.d(TAG, "Running main module");
        py.getModule("runpy").callAttr("run_module", "helloworld",
                                       new Kwarg("run_name", "__main__"),
                                       new Kwarg("alter_sys", true));

        userCode("onCreate");
        Log.d(TAG, "onCreate() complete");
    }

    protected void onStart() {
        Log.d(TAG, "onStart() start");
        super.onStart();
        userCode("onStart");
        Log.d(TAG, "onStart() complete");
    }

    protected void onResume() {
        Log.d(TAG, "onResume() start");
        super.onResume();
        userCode("onResume");
        Log.d(TAG, "onResume() complete");
    }

    protected void onActivityResult(int requestCode, int resultCode, Intent data)
    {
        Log.d(TAG, "onActivityResult() start");
        super.onActivityResult(requestCode, resultCode, data);
        userCode("onActivityResult", requestCode, resultCode, data);
        Log.d(TAG, "onActivityResult() complete");
    }

    public void onConfigurationChanged(Configuration newConfig) {
        Log.d(TAG, "onConfigurationChanged() start");
        super.onConfigurationChanged(newConfig);
        userCode("onConfigurationChanged", newConfig);
        Log.d(TAG, "onConfigurationChanged() complete");
    }

    public boolean onOptionsItemSelected(MenuItem menuitem) {
        Log.d(TAG, "onOptionsItemSelected() start");
        PyObject pyResult = userCode("onOptionsItemSelected", menuitem);
        boolean result = (pyResult == null) ? false : pyResult.toBoolean();
        Log.d(TAG, "onOptionsItemSelected() complete");
        return result;
    }

    public boolean onPrepareOptionsMenu(Menu menu) {
        Log.d(TAG, "onPrepareOptionsMenu() start");
        PyObject pyResult = userCode("onPrepareOptionsMenu", menu);
        boolean result = (pyResult == null) ? false : pyResult.toBoolean();
        Log.d(TAG, "onPrepareOptionsMenu() complete");
        return result;
    }

    private PyObject userCode(String methodName, Object... args) {
        if (pythonApp == null) {
            // Could be a non-graphical app such as Python-support-testbed.
            return null;
        }
        try {
            return pythonApp.callAttr(methodName, args);
        } catch (PyException e) {
            if (e.getMessage().startsWith("NotImplementedError")) {
                return null;
            }
            throw e;
        }
    }

    private native boolean captureStdoutStderr();

    static {
        System.loadLibrary("native-lib");
    }
}
