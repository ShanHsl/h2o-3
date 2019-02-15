import h2o
import tempfile
from h2o.estimators import H2OGeneralizedLinearEstimator, H2OGenericEstimator
from tests import pyunit_utils


def mojo_model_glm_test():

    # GLM
    airlines = h2o.import_file(path=pyunit_utils.locate("smalldata/testng/airlines_train.csv"))
    glm = H2OGeneralizedLinearEstimator()
    glm.train(x = ["Origin", "Dest"], y = "Distance", training_frame=airlines)

    filename = tempfile.mkdtemp()
    filename = glm.download_mojo(filename)
      
    model = H2OGenericEstimator.from_mojo_file(filename)
    assert model is not None
    predictions = model.predict(airlines)
    assert predictions is not None
    assert predictions.nrows == 24421
    
if __name__ == "__main__":
    pyunit_utils.standalone_test(mojo_model_glm_test)
else:
    mojo_model_glm_test()