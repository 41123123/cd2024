﻿# NX 1872
# Journal created by User on Fri Jun 14 17:42:13 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Drawings
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    # ----------------------------------------------
    #   功能表：檔案(F)->新建(N)...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    fileNew1 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId1, "新建 對話方塊")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新建")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "新建")
    
    fileNew1.TemplateFileName = "model-plain-1-mm-template.prt"
    
    fileNew1.UseBlankTemplate = False
    
    fileNew1.ApplicationName = "ModelTemplate"
    
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    
    fileNew1.RelationType = ""
    
    fileNew1.UsesMasterModel = "No"
    
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew1.TemplatePresentationName = "模型"
    
    fileNew1.ItemType = ""
    
    fileNew1.Specialization = ""
    
    fileNew1.SetCanCreateAltrep(False)
    
    fileNew1.NewFileName = "Z:\\model1.prt"
    
    fileNew1.MasterFileName = ""
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    nXObject1 = fileNew1.Commit()
    
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    theSession.DeleteUndoMark(markId3, None)
    
    fileNew1.Destroy()
    
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit1 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId4, "拉伸 對話方塊")
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    datumAxis1 = workPart.Datums.FindObject("DATUM_CSYS(0) Y axis")
    direction1 = workPart.Directions.CreateDirection(datumAxis1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumPlane1 = workPart.Datums.FindObject("DATUM_CSYS(0) YZ plane")
    datumCsys1 = workPart.Features.FindObject("DATUM_CSYS(0)")
    point1 = datumCsys1.FindObject("POINT 1")
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(datumPlane1, direction1, point1, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder1 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder1.Csys = cartesianCoordinateSystem1
    
    datumCsysBuilder1.DisplayScaleFactor = 1.25
    
    feature1 = datumCsysBuilder1.CommitFeature()
    
    datumCsysBuilder1.Destroy()
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder1.Csystem = cartesianCoordinateSystem1
    
    sketchInPlaceBuilder1.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject2 = sketchInPlaceBuilder1.Commit()
    
    sketchInPlaceBuilder1.Destroy()
    
    sketch1 = nXObject2
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId6, None, True)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_000")
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   對話開始 輪廓
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->曲線(C)->圓(C)...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId8, "Curve")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   功能表：插入(S)->曲線(C)->矩形(R)...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId9, "Curve")
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Rectangle")
    
    theSession.SetUndoMarkVisibility(markId11, "Create Rectangle", NXOpen.Session.MarkVisibility.Visible)
    
    # ----------------------------------------------
    # Creating rectangle using By 2 Points method 
    # ----------------------------------------------
    startPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    endPoint1 = NXOpen.Point3d(0.0, 106.0, 0.0)
    line1 = workPart.Curves.CreateLine(startPoint1, endPoint1)
    
    startPoint2 = NXOpen.Point3d(0.0, 106.0, 0.0)
    endPoint2 = NXOpen.Point3d(0.0, 106.0, 59.0)
    line2 = workPart.Curves.CreateLine(startPoint2, endPoint2)
    
    startPoint3 = NXOpen.Point3d(0.0, 106.0, 59.0)
    endPoint3 = NXOpen.Point3d(0.0, 0.0, 59.0)
    line3 = workPart.Curves.CreateLine(startPoint3, endPoint3)
    
    startPoint4 = NXOpen.Point3d(0.0, 0.0, 59.0)
    endPoint4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    line4 = workPart.Curves.CreateLine(startPoint4, endPoint4)
    
    theSession.ActiveSketch.AddGeometry(line1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.AddGeometry(line4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    geom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_1.Geometry = line1
    geom1_1.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_1.SplineDefiningPointIndex = 0
    geom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_1.Geometry = line2
    geom2_1.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint1 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_1, geom2_1)
    
    geom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_2.Geometry = line2
    geom1_2.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_2.SplineDefiningPointIndex = 0
    geom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_2.Geometry = line3
    geom2_2.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint2 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_2, geom2_2)
    
    geom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_3.Geometry = line3
    geom1_3.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_3.SplineDefiningPointIndex = 0
    geom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_3.Geometry = line4
    geom2_3.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint3 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_3, geom2_3)
    
    geom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_4.Geometry = line4
    geom1_4.PointType = NXOpen.Sketch.ConstraintPointType.EndVertex
    geom1_4.SplineDefiningPointIndex = 0
    geom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    geom2_4.Geometry = line1
    geom2_4.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint4 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_4, geom2_4)
    
    geom1 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1.Geometry = line1
    geom1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint5 = theSession.ActiveSketch.CreateHorizontalConstraint(geom1)
    
    conGeom1_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_1.Geometry = line1
    conGeom1_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_1.SplineDefiningPointIndex = 0
    conGeom2_1 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_1.Geometry = line2
    conGeom2_1.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_1.SplineDefiningPointIndex = 0
    sketchGeometricConstraint6 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_1, conGeom2_1)
    
    conGeom1_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_2.Geometry = line2
    conGeom1_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_2.SplineDefiningPointIndex = 0
    conGeom2_2 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_2.Geometry = line3
    conGeom2_2.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_2.SplineDefiningPointIndex = 0
    sketchGeometricConstraint7 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_2, conGeom2_2)
    
    conGeom1_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_3.Geometry = line3
    conGeom1_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_3.SplineDefiningPointIndex = 0
    conGeom2_3 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_3.Geometry = line4
    conGeom2_3.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_3.SplineDefiningPointIndex = 0
    sketchGeometricConstraint8 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_3, conGeom2_3)
    
    conGeom1_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom1_4.Geometry = line4
    conGeom1_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom1_4.SplineDefiningPointIndex = 0
    conGeom2_4 = NXOpen.Sketch.ConstraintGeometry()
    
    conGeom2_4.Geometry = line1
    conGeom2_4.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    conGeom2_4.SplineDefiningPointIndex = 0
    sketchGeometricConstraint9 = theSession.ActiveSketch.CreatePerpendicularConstraint(conGeom1_4, conGeom2_4)
    
    geom1_5 = NXOpen.Sketch.ConstraintGeometry()
    
    geom1_5.Geometry = line1
    geom1_5.PointType = NXOpen.Sketch.ConstraintPointType.StartVertex
    geom1_5.SplineDefiningPointIndex = 0
    geom2_5 = NXOpen.Sketch.ConstraintGeometry()
    
    datumCsys2 = feature1
    point2 = datumCsys2.FindObject("POINT 1")
    geom2_5.Geometry = point2
    geom2_5.PointType = NXOpen.Sketch.ConstraintPointType.NotSet
    geom2_5.SplineDefiningPointIndex = 0
    sketchGeometricConstraint10 = theSession.ActiveSketch.CreateCoincidentConstraint(geom1_5, geom2_5)
    
    dimObject1_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_1.Geometry = line1
    dimObject1_1.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_1.AssocValue = 0
    dimObject1_1.HelpPoint.X = 0.0
    dimObject1_1.HelpPoint.Y = 0.0
    dimObject1_1.HelpPoint.Z = 0.0
    dimObject1_1.View = NXOpen.NXObject.Null
    dimObject2_1 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_1.Geometry = line1
    dimObject2_1.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_1.AssocValue = 0
    dimObject2_1.HelpPoint.X = 0.0
    dimObject2_1.HelpPoint.Y = 0.0
    dimObject2_1.HelpPoint.Z = 0.0
    dimObject2_1.View = NXOpen.NXObject.Null
    dimOrigin1 = NXOpen.Point3d(0.0, 53.0, -9.9368099155661405)
    sketchDimensionalConstraint1 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_1, dimObject2_1, dimOrigin1, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint1 = sketchDimensionalConstraint1
    dimension1 = sketchHelpedDimensionalConstraint1.AssociatedDimension
    
    expression2 = sketchHelpedDimensionalConstraint1.AssociatedExpression
    
    dimObject1_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_2.Geometry = line2
    dimObject1_2.AssocType = NXOpen.Sketch.AssocType.StartPoint
    dimObject1_2.AssocValue = 0
    dimObject1_2.HelpPoint.X = 0.0
    dimObject1_2.HelpPoint.Y = 0.0
    dimObject1_2.HelpPoint.Z = 0.0
    dimObject1_2.View = NXOpen.NXObject.Null
    dimObject2_2 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject2_2.Geometry = line2
    dimObject2_2.AssocType = NXOpen.Sketch.AssocType.EndPoint
    dimObject2_2.AssocValue = 0
    dimObject2_2.HelpPoint.X = 0.0
    dimObject2_2.HelpPoint.Y = 0.0
    dimObject2_2.HelpPoint.Z = 0.0
    dimObject2_2.View = NXOpen.NXObject.Null
    dimOrigin2 = NXOpen.Point3d(0.0, 115.93680991556614, 29.5)
    sketchDimensionalConstraint2 = theSession.ActiveSketch.CreateDimension(NXOpen.Sketch.ConstraintType.ParallelDim, dimObject1_2, dimObject2_2, dimOrigin2, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    sketchHelpedDimensionalConstraint2 = sketchDimensionalConstraint2
    dimension2 = sketchHelpedDimensionalConstraint2.AssociatedDimension
    
    expression3 = sketchHelpedDimensionalConstraint2.AssociatedExpression
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = False
    
    theSession.ActiveSketch.Update()
    
    theSession.Preferences.Sketch.AutoDimensionsToArcCenter = True
    
    geoms1 = [NXOpen.SmartObject.Null] * 4 
    geoms1[0] = line1
    geoms1[1] = line2
    geoms1[2] = line3
    geoms1[3] = line4
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms1)
    
    geoms2 = [NXOpen.SmartObject.Null] * 4 
    geoms2[0] = line1
    geoms2[1] = line2
    geoms2[2] = line3
    geoms2[3] = line4
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms2)
    
    # ----------------------------------------------
    #   功能表：插入(S)->尺寸(M)->快速(P)...
    # ----------------------------------------------
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder1 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    sketchRapidDimensionBuilder1.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.ModelView
    
    lines1 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBefore(lines1)
    
    lines2 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAfter(lines2)
    
    lines3 = []
    sketchRapidDimensionBuilder1.AppendedText.SetAbove(lines3)
    
    lines4 = []
    sketchRapidDimensionBuilder1.AppendedText.SetBelow(lines4)
    
    theSession.SetUndoMarkName(markId12, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder1.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.ModelView
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits1 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits2 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits3 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits4 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits5 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits6 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits7 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits8 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits9 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits10 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder1.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder1.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder1.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits11 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits12 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits13 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits14 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits15 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits16 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits17 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits18 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits19 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits20 = sketchRapidDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    parallelDimension1 = dimension2
    point3 = NXOpen.Point3d(0.0, 116.99558591212924, 28.628133381744497)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(parallelDimension1, workPart.ModelingViews.WorkView, point3)
    
    point1_1 = NXOpen.Point3d(0.0, 106.0, 0.0)
    point2_1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Start, line2, NXOpen.View.Null, point1_1, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_1)
    
    point1_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_2, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_2)
    
    sketchRapidDimensionBuilder1.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    convertToFromReferenceBuilder1 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList1 = convertToFromReferenceBuilder1.InputObjects
    
    added1 = selectNXObjectList1.Add(parallelDimension1)
    
    convertToFromReferenceBuilder1.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject3 = convertToFromReferenceBuilder1.Commit()
    
    convertToFromReferenceBuilder1.Destroy()
    
    expression4 = workPart.Expressions.FindObject("p7")
    expression4.SetFormula("50")
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.Scale(0.84745762711864403)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId13, None)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId12, "Edit Driving Value")
    
    parallelDimension2 = dimension1
    point4 = NXOpen.Point3d(0.0, 49.80710960803502, -10.516457160640821)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(parallelDimension2, workPart.ModelingViews.WorkView, point4)
    
    point1_3 = NXOpen.Point3d(0.0, 89.830508474576263, 0.0)
    point2_3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.End, line1, NXOpen.View.Null, point1_3, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_3)
    
    point1_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder1.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_4, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_4)
    
    sketchRapidDimensionBuilder1.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    convertToFromReferenceBuilder2 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList2 = convertToFromReferenceBuilder2.InputObjects
    
    added2 = selectNXObjectList2.Add(parallelDimension2)
    
    convertToFromReferenceBuilder2.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject4 = convertToFromReferenceBuilder2.Commit()
    
    convertToFromReferenceBuilder2.Destroy()
    
    expression5 = workPart.Expressions.FindObject("p8")
    expression5.SetFormula("100")
    
    theSession.SetUndoMarkVisibility(markId14, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId15, None)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId14, "Edit Driving Value")
    
    # ----------------------------------------------
    #   功能表：任務(K)->完成草圖(K)
    # ----------------------------------------------
    sketchRapidDimensionBuilder1.Destroy()
    
    theSession.UndoToMark(markId16, None)
    
    theSession.DeleteUndoMark(markId16, None)
    
    sketchRapidDimensionBuilder1.Destroy()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId5, None)
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves1 = [NXOpen.ICurve.Null] * 4 
    curves1[0] = line2
    curves1[1] = line3
    curves1[2] = line1
    curves1[3] = line4
    seedPoint1 = NXOpen.Point3d(0.0, 33.333333333333336, 33.333333333333336)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch1, curves1, seedPoint1, 0.01)
    
    section1.AllowSelfIntersection(True)
    
    rules1 = [None] * 1 
    rules1[0] = regionBoundaryRule1
    helpPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section1.AddToSection(rules1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId18, None)
    
    unit2 = extrudeBuilder1.Offset.StartOffset.Units
    
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs1 = section1.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression6)
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction2 = workPart.Directions.CreateDirection(sketch1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("50")
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId19, None)
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder1.ParentFeatureInternal = True
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId20, None)
    
    theSession.SetUndoMarkName(markId4, "拉伸")
    
    expression8 = extrudeBuilder1.Limits.StartExtend.Value
    expression9 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression1)
    
    workPart.Expressions.Delete(expression7)
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.067968277872691274
    rotMatrix1.Xy = 0.98228641037603293
    rotMatrix1.Xz = 0.17462451487001546
    rotMatrix1.Yx = -0.39840843433709805
    rotMatrix1.Yy = -0.13374504563379214
    rotMatrix1.Yz = 0.90740453063530435
    rotMatrix1.Zx = 0.91468630286677111
    rotMatrix1.Zy = -0.1312466028473975
    rotMatrix1.Zz = 0.38226077040279005
    translation1 = NXOpen.Point3d(-0.61843372745717673, 21.702894291615255, -27.756469285511354)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.90572327300951838)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.28866279366458603
    rotMatrix2.Xy = 0.93715252435327878
    rotMatrix2.Xz = 0.19600749386702357
    rotMatrix2.Yx = 0.13402909500093704
    rotMatrix2.Yy = -0.24226002688594594
    rotMatrix2.Yz = 0.96090909094796595
    rotMatrix2.Zx = 0.94800316098997284
    rotMatrix2.Zy = -0.25110799563433889
    rotMatrix2.Zz = -0.19553716087106943
    translation2 = NXOpen.Point3d(-4.4136767960420364, 12.480091112955524, -8.1513728173978386)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.90572327300951838)
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Feature Parameters")
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "起點")
    
    extrude1 = feature2
    extrudeBuilder2 = workPart.Features.CreateExtrudeBuilder(extrude1)
    
    section1.PrepareMappingData()
    
    extrudeBuilder2.AllowSelfIntersectingSection(True)
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.SetUndoMarkName(markId22, "拉伸 對話方塊")
    
    sketchFeature1 = workPart.Features.FindObject("EXTRUDE(1:1B)")
    extrudeBuilder2.ShowInternalParentFeatureForEdit(sketchFeature1)
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    # ----------------------------------------------
    #   對話開始 拉伸
    # ----------------------------------------------
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.025791849163734559
    rotMatrix3.Xy = 0.99895860855509344
    rotMatrix3.Xz = 0.037636138356442722
    rotMatrix3.Yx = -0.085544648446130467
    rotMatrix3.Yy = -0.035305039296496782
    rotMatrix3.Yz = 0.9957086257146196
    rotMatrix3.Zx = 0.99600044861382264
    rotMatrix3.Zy = -0.028900736910032046
    rotMatrix3.Zz = 0.084544980732825112
    translation3 = NXOpen.Point3d(2.1010922035770712, 5.1282334204433155, -28.57237338805108)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 0.90572327300951838)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId24, None)
    
    workPart.Expressions.Delete(expression11)
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    theSession.DeleteUndoMark(markId23, None)
    
    expression4.SetFormula("30")
    
    sketch1.LocalUpdate()
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId25, None)
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    feature3 = extrudeBuilder2.CommitFeature()
    
    theSession.DeleteUndoMark(markId26, None)
    
    theSession.SetUndoMarkName(markId22, "拉伸")
    
    section1.CleanMappingData()
    
    expression13 = extrudeBuilder2.Limits.StartExtend.Value
    expression14 = extrudeBuilder2.Limits.EndExtend.Value
    extrudeBuilder2.Destroy()
    
    workPart.Expressions.Delete(expression10)
    
    workPart.Expressions.Delete(expression12)
    
    theSession.DeleteUndoMark(markId22, None)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId21)
    
    theSession.Preferences.Modeling.UpdatePending = False
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.29253473165271088
    rotMatrix4.Xy = 0.95361989438648043
    rotMatrix4.Xz = 0.070940311580892965
    rotMatrix4.Yx = 0.33980902429627086
    rotMatrix4.Yy = -0.17301055274285188
    rotMatrix4.Yz = 0.9244442523194295
    rotMatrix4.Zx = 0.89384185278140316
    rotMatrix4.Zy = -0.24632589321857842
    rotMatrix4.Zz = -0.37466024148069998
    translation4 = NXOpen.Point3d(-2.8001067485834348, 2.4486328751288884, -8.2590723436103914)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 0.90572327300951838)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder3 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section2 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder3.Section = section2
    
    extrudeBuilder3.AllowSelfIntersectingSection(True)
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder3.DistanceTolerance = 0.01
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies2)
    
    extrudeBuilder3.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder3.Limits.EndExtend.Value.SetFormula("50")
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies3 = [NXOpen.Body.Null] * 1 
    targetBodies3[0] = NXOpen.Body.Null
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies3)
    
    extrudeBuilder3.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder3.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder3.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder2 = extrudeBuilder3.SmartVolumeProfile
    
    smartVolumeProfileBuilder2.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder2.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId27, "拉伸 對話方塊")
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    section2.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar1 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrude2 = feature3
    edge1 = extrude2.FindObject("EDGE * 130 * 140 {(50,-0,30)(50,-0,15)(50,0,0) EXTRUDE(1)}")
    point5 = workPart.Points.CreatePoint(edge1, scalar1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge2 = extrude2.FindObject("EDGE * 130 * 150 {(50,0,0)(50,50,0)(50,100,0) EXTRUDE(1)}")
    direction3 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face1 = extrude2.FindObject("FACE 130 {(50,50,15) EXTRUDE(1)}")
    xform2 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction3, point5, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder2 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder2.Csys = cartesianCoordinateSystem2
    
    datumCsysBuilder2.DisplayScaleFactor = 1.25
    
    feature4 = datumCsysBuilder2.CommitFeature()
    
    datumCsysBuilder2.Destroy()
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder2 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder2.Csystem = cartesianCoordinateSystem2
    
    sketchInPlaceBuilder2.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject5 = sketchInPlaceBuilder2.Commit()
    
    sketchInPlaceBuilder2.Destroy()
    
    sketch2 = nXObject5
    sketch2.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId29, None, True)
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   對話開始 輪廓
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->曲線(C)->圓(C)...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId31, "Curve")
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    scaleAboutPoint1 = NXOpen.Point3d(56.525957238444427, 21.325038131299475, 0.0)
    viewCenter1 = NXOpen.Point3d(-56.525957238444427, -21.325038131299475, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(41.715280070541937, 15.657836216954127, 0.0)
    viewCenter2 = NXOpen.Point3d(-41.715280070541937, -15.657836216954127, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(32.250468625965205, 12.526268973563301, 0.0)
    viewCenter3 = NXOpen.Point3d(-32.250468625965205, -12.526268973563301, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    scaleAboutPoint4 = NXOpen.Point3d(25.800374900772155, 10.021015178850639, 0.0)
    viewCenter4 = NXOpen.Point3d(-25.800374900772155, -10.021015178850639, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint4, viewCenter4)
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId33, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(50.0, 52.0, 19.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 4.215152020915454, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_3 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_3.Geometry = arc1
    dimObject1_3.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_3.AssocValue = 0
    dimObject1_3.HelpPoint.X = 0.0
    dimObject1_3.HelpPoint.Y = 0.0
    dimObject1_3.HelpPoint.Z = 0.0
    dimObject1_3.View = NXOpen.NXObject.Null
    dimOrigin3 = NXOpen.Point3d(50.0, 52.0, 20.356705780471962)
    sketchDimensionalConstraint3 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_3, dimOrigin3, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension3 = sketchDimensionalConstraint3.AssociatedDimension
    
    expression16 = sketchDimensionalConstraint3.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   對話開始 圓
    # ----------------------------------------------
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    perpendicularDimension1 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    sketchLinearDimensionBuilder1 = workPart.Sketches.CreateLinearDimensionBuilder(perpendicularDimension1)
    
    sketchLinearDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Inferred
    
    sketchLinearDimensionBuilder1.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId34, "線性尺寸 對話方塊")
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits21 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits22 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder1.Style.OrdinateStyle.DoglegCreationOption = NXOpen.Annotations.OrdinateDoglegCreationOption.No
    
    dimensionlinearunits23 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits24 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits25 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits26 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder1.Measurement.Direction = NXOpen.Direction.Null
    
    sketchLinearDimensionBuilder1.Measurement.DirectionView = NXOpen.View.Null
    
    sketchLinearDimensionBuilder1.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits27 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits28 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits29 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits30 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits31 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits32 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits33 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits34 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits35 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits36 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits37 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits38 = sketchLinearDimensionBuilder1.Style.UnitsStyle.DimensionLinearUnits
    
    # ----------------------------------------------
    #   對話開始 線性尺寸
    # ----------------------------------------------
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    theSession.DeleteUndoMark(markId35, None)
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    theSession.SetUndoMarkName(markId34, "線性尺寸")
    
    expression17 = sketchLinearDimensionBuilder1.Driving.ExpressionValue
    sketchLinearDimensionBuilder1.Destroy()
    
    theSession.DeleteUndoMark(markId36, None)
    
    theSession.DeleteUndoMark(markId34, None)
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    perpendicularDimension2 = theSession.ActiveSketch.FindObject("ENTITY 26 2 1")
    sketchLinearDimensionBuilder2 = workPart.Sketches.CreateLinearDimensionBuilder(perpendicularDimension2)
    
    sketchLinearDimensionBuilder2.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Inferred
    
    sketchLinearDimensionBuilder2.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId37, "線性尺寸 對話方塊")
    
    sketchLinearDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits39 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits40 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder2.Style.OrdinateStyle.DoglegCreationOption = NXOpen.Annotations.OrdinateDoglegCreationOption.No
    
    dimensionlinearunits41 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits42 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits43 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits44 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchLinearDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchLinearDimensionBuilder2.Measurement.Direction = NXOpen.Direction.Null
    
    sketchLinearDimensionBuilder2.Measurement.DirectionView = NXOpen.View.Null
    
    sketchLinearDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits45 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits46 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits47 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits48 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits49 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits50 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits51 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits52 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits53 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits54 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits55 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits56 = sketchLinearDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    # ----------------------------------------------
    #   對話開始 線性尺寸
    # ----------------------------------------------
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    theSession.DeleteUndoMark(markId38, None)
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    sketchLinearDimensionBuilder2.Driving.ExpressionValue.SetFormula("24")
    
    sketchLinearDimensionBuilder2.Driving.ExpressionMode = NXOpen.Annotations.DrivingValueBuilder.DrivingExpressionMode.KeepExpression
    
    sketchLinearDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    nXObject6 = sketchLinearDimensionBuilder2.Commit()
    
    taggedObject1 = sketchLinearDimensionBuilder2.FirstAssociativity.Value
    
    line5 = taggedObject1
    point1_5 = NXOpen.Point3d(50.0, 14.2875, 0.0)
    point2_5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchLinearDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line5, NXOpen.View.Null, point1_5, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_5)
    
    point1_6 = NXOpen.Point3d(50.0, 52.0, 24.0)
    point2_6 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchLinearDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc1, NXOpen.View.Null, point1_6, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_6)
    
    sketchLinearDimensionBuilder2.Driving.ExpressionValue.SetFormula("24")
    
    theSession.SetUndoMarkName(markId39, "線性尺寸 - =")
    
    theSession.SetUndoMarkVisibility(markId39, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.SetUndoMarkVisibility(markId37, None, NXOpen.Session.MarkVisibility.Invisible)
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    # ----------------------------------------------
    #   功能表：任務(K)->完成草圖(K)
    # ----------------------------------------------
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "線性尺寸")
    
    nXObject7 = sketchLinearDimensionBuilder2.Commit()
    
    theSession.DeleteUndoMark(markId41, None)
    
    theSession.SetUndoMarkName(markId37, "線性尺寸")
    
    expression18 = sketchLinearDimensionBuilder2.Driving.ExpressionValue
    sketchLinearDimensionBuilder2.Destroy()
    
    theSession.DeleteUndoMark(markId40, None)
    
    theSession.SetUndoMarkVisibility(markId37, None, NXOpen.Session.MarkVisibility.Visible)
    
    theSession.DeleteUndoMark(markId39, None)
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId28, None)
    
    section2.DistanceTolerance = 0.01
    
    section2.ChainingTolerance = 0.0094999999999999998
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves2 = [NXOpen.ICurve.Null] * 1 
    curves2[0] = arc1
    seedPoint2 = NXOpen.Point3d(50.0, 53.405050673638485, 23.999999999999996)
    regionBoundaryRule2 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch2, curves2, seedPoint2, 0.01)
    
    section2.AllowSelfIntersection(True)
    
    rules2 = [None] * 1 
    rules2[0] = regionBoundaryRule2
    helpPoint2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section2.AddToSection(rules2, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint2, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId43, None)
    
    expression19 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs2 = section2.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression19)
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction4 = workPart.Directions.CreateDirection(sketch2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder3.Direction = direction4
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    body1 = workPart.Bodies.FindObject("EXTRUDE(1)")
    targetBodies4[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies4)
    
    extrudeBuilder3.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies5 = [NXOpen.Body.Null] * 1 
    targetBodies5[0] = body1
    extrudeBuilder3.BooleanOperation.SetTargetBodies(targetBodies5)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = -0.019345048198660959
    rotMatrix5.Xy = 0.99213004449176356
    rotMatrix5.Xz = 0.12370830177057711
    rotMatrix5.Yx = 0.080556068070383791
    rotMatrix5.Yy = -0.12178251215265712
    rotMatrix5.Yz = 0.98928243673423522
    rotMatrix5.Zx = 0.9965623357358161
    rotMatrix5.Zy = 0.029103170799015442
    rotMatrix5.Zz = -0.077566206831403639
    translation5 = NXOpen.Point3d(2.2798603895914447, 5.3959819850442443, -29.054948138089859)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 0.90572327300951838)
    
    extrudeBuilder3.Destroy()
    
    section2.Destroy()
    
    workPart.Expressions.Delete(expression15)
    
    workPart.Expressions.Delete(expression20)
    
    theSession.UndoToMark(markId27, None)
    
    theSession.DeleteUndoMark(markId27, None)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder4 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section3 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder4.Section = section3
    
    extrudeBuilder4.AllowSelfIntersectingSection(True)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder4.DistanceTolerance = 0.01
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies6 = [NXOpen.Body.Null] * 1 
    targetBodies6[0] = NXOpen.Body.Null
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies6)
    
    extrudeBuilder4.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("50")
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies7 = [NXOpen.Body.Null] * 1 
    targetBodies7[0] = NXOpen.Body.Null
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies7)
    
    extrudeBuilder4.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder4.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder4.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder4.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder3 = extrudeBuilder4.SmartVolumeProfile
    
    smartVolumeProfileBuilder3.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder3.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId44, "拉伸 對話方塊")
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    section3.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar2 = workPart.Scalars.CreateScalar(0.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point6 = workPart.Points.CreatePoint(edge1, scalar2, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction5 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform3 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction5, point6, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem3 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder3 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder3.Csys = cartesianCoordinateSystem3
    
    datumCsysBuilder3.DisplayScaleFactor = 1.25
    
    feature5 = datumCsysBuilder3.CommitFeature()
    
    datumCsysBuilder3.Destroy()
    
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder3 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder3.Csystem = cartesianCoordinateSystem3
    
    sketchInPlaceBuilder3.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject8 = sketchInPlaceBuilder3.Commit()
    
    sketchInPlaceBuilder3.Destroy()
    
    sketch3 = nXObject8
    sketch3.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId46, None, True)
    
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_001")
    
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   對話開始 輪廓
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->曲線(C)->圓(C)...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId48, "Curve")
    
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    scaleAboutPoint5 = NXOpen.Point3d(36.953661967251769, -11.100704780676436, 0.0)
    viewCenter5 = NXOpen.Point3d(-36.953661967251769, 11.100704780676436, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint5, viewCenter5)
    
    scaleAboutPoint6 = NXOpen.Point3d(29.562929573801412, -8.8805638245411274, 0.0)
    viewCenter6 = NXOpen.Point3d(-29.562929573801412, 8.8805638245411682, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(23.650343659041127, -6.9174918212215051, 0.0)
    viewCenter7 = NXOpen.Point3d(-23.650343659041127, 6.9174918212215379, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId50, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(50.0, 51.0, 18.999999999999989)
    arc2 = workPart.Curves.CreateArc(center2, nXMatrix2, 5.6613894083049949, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_4 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_4.Geometry = arc2
    dimObject1_4.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_4.AssocValue = 0
    dimObject1_4.HelpPoint.X = 0.0
    dimObject1_4.HelpPoint.Y = 0.0
    dimObject1_4.HelpPoint.Z = 0.0
    dimObject1_4.View = NXOpen.NXObject.Null
    dimOrigin4 = NXOpen.Point3d(50.0, 51.0, 20.695882225589944)
    sketchDimensionalConstraint4 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_4, dimOrigin4, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension4 = sketchDimensionalConstraint4.AssociatedDimension
    
    expression22 = sketchDimensionalConstraint4.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   對話開始 圓
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->尺寸(M)->快速(P)...
    # ----------------------------------------------
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder2 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    sketchRapidDimensionBuilder2.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.ModelView
    
    lines5 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBefore(lines5)
    
    lines6 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAfter(lines6)
    
    lines7 = []
    sketchRapidDimensionBuilder2.AppendedText.SetAbove(lines7)
    
    lines8 = []
    sketchRapidDimensionBuilder2.AppendedText.SetBelow(lines8)
    
    theSession.SetUndoMarkName(markId51, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder2.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.ModelView
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits57 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits58 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits59 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits60 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits61 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits62 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits63 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits64 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits65 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits66 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder2.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder2.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder2.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder2.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits67 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits68 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits69 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits70 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits71 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits72 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits73 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits74 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits75 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits76 = sketchRapidDimensionBuilder2.Style.UnitsStyle.DimensionLinearUnits
    
    convertToFromReferenceBuilder3 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList3 = convertToFromReferenceBuilder3.InputObjects
    
    diameterDimension1 = dimension4
    added3 = selectNXObjectList3.Add(diameterDimension1)
    
    convertToFromReferenceBuilder3.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject9 = convertToFromReferenceBuilder3.Commit()
    
    convertToFromReferenceBuilder3.Destroy()
    
    expression23 = workPart.Expressions.FindObject("p16")
    expression23.SetFormula("10")
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.Scale(0.88317542557048412)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId52, None)
    
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId51, "Edit Driving Value")
    
    perpendicularDimension3 = theSession.ActiveSketch.FindObject("ENTITY 26 2 1")
    point7 = NXOpen.Point3d(100.0, 50.115592351413824, 27.312460947836279)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(perpendicularDimension3, workPart.ModelingViews.WorkView, point7)
    
    line6 = theSession.ActiveSketch.FindObject("Curve DATUM1")
    point1_7 = NXOpen.Point3d(50.0, 14.2875, 29.999999999999989)
    point2_7 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line6, NXOpen.View.Null, point1_7, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_7)
    
    point1_8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_8 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_8, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_8)
    
    sketchRapidDimensionBuilder2.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    convertToFromReferenceBuilder4 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList4 = convertToFromReferenceBuilder4.InputObjects
    
    added4 = selectNXObjectList4.Add(perpendicularDimension3)
    
    convertToFromReferenceBuilder4.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject10 = convertToFromReferenceBuilder4.Commit()
    
    convertToFromReferenceBuilder4.Destroy()
    
    expression24 = workPart.Expressions.FindObject("p17")
    expression24.SetFormula("6")
    
    theSession.SetUndoMarkVisibility(markId53, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId54, None)
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId53, "Edit Driving Value")
    
    perpendicularDimension4 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    point8 = NXOpen.Point3d(50.0, 20.774758223747632, 18.338417504089428)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(perpendicularDimension4, workPart.ModelingViews.WorkView, point8)
    
    line7 = theSession.ActiveSketch.FindObject("Curve DATUM2")
    point1_9 = NXOpen.Point3d(50.0, -3.0616169978683748e-16, 44.287499999999987)
    point2_9 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line7, NXOpen.View.Null, point1_9, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_9)
    
    point1_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_10 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder2.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_10, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_10)
    
    sketchRapidDimensionBuilder2.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    convertToFromReferenceBuilder5 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList5 = convertToFromReferenceBuilder5.InputObjects
    
    added5 = selectNXObjectList5.Add(perpendicularDimension4)
    
    convertToFromReferenceBuilder5.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject11 = convertToFromReferenceBuilder5.Commit()
    
    convertToFromReferenceBuilder5.Destroy()
    
    expression25 = workPart.Expressions.FindObject("p18")
    expression25.SetFormula("50")
    
    theSession.SetUndoMarkVisibility(markId55, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId56, None)
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId55, "Edit Driving Value")
    
    sketchRapidDimensionBuilder2.Destroy()
    
    theSession.UndoToMark(markId57, None)
    
    theSession.DeleteUndoMark(markId57, None)
    
    sketchRapidDimensionBuilder2.Destroy()
    
    # ----------------------------------------------
    #   功能表：任務(K)->完成草圖(K)
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId45, None)
    
    section3.DistanceTolerance = 0.01
    
    section3.ChainingTolerance = 0.0094999999999999998
    
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves3 = [NXOpen.ICurve.Null] * 1 
    curves3[0] = arc2
    seedPoint3 = NXOpen.Point3d(50.0, 50.0, 22.333333333333314)
    regionBoundaryRule3 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch3, curves3, seedPoint3, 0.01)
    
    section3.AllowSelfIntersection(True)
    
    rules3 = [None] * 1 
    rules3[0] = regionBoundaryRule3
    helpPoint3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section3.AddToSection(rules3, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint3, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId59, None)
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs3 = section3.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression26)
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction6 = workPart.Directions.CreateDirection(sketch3, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder4.Direction = direction6
    
    targetBodies8 = [NXOpen.Body.Null] * 1 
    targetBodies8[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies8)
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Unite
    
    targetBodies9 = [NXOpen.Body.Null] * 1 
    targetBodies9[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies9)
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = 0.41094361794248535
    rotMatrix6.Xy = 0.88826337458383531
    rotMatrix6.Xz = 0.20521578946385474
    rotMatrix6.Yx = -0.51388548958302782
    rotMatrix6.Yy = 0.039764129336750359
    rotMatrix6.Yz = 0.85693670572224645
    rotMatrix6.Zx = 0.75302526283541227
    rotMatrix6.Zy = -0.45761008663601649
    rotMatrix6.Zz = 0.47280647430066641
    translation6 = NXOpen.Point3d(-4.5066350839399725, 14.164874817088993, -6.8864486608092159)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 0.90572327300951838)
    
    extrudeBuilder4.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies10 = [NXOpen.Body.Null] * 1 
    targetBodies10[0] = body1
    extrudeBuilder4.BooleanOperation.SetTargetBodies(targetBodies10)
    
    direction7 = extrudeBuilder4.Direction
    
    success1 = direction7.ReverseDirection()
    
    extrudeBuilder4.Direction = direction7
    
    extrudeBuilder4.Limits.EndExtend.Value.SetFormula("85")
    
    markId60 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId60, None)
    
    markId61 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder4.ParentFeatureInternal = True
    
    feature6 = extrudeBuilder4.CommitFeature()
    
    theSession.DeleteUndoMark(markId61, None)
    
    theSession.SetUndoMarkName(markId44, "拉伸")
    
    expression28 = extrudeBuilder4.Limits.StartExtend.Value
    expression29 = extrudeBuilder4.Limits.EndExtend.Value
    extrudeBuilder4.Destroy()
    
    workPart.Expressions.Delete(expression21)
    
    workPart.Expressions.Delete(expression27)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId62 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder5 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section4 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder5.Section = section4
    
    extrudeBuilder5.AllowSelfIntersectingSection(True)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder5.DistanceTolerance = 0.01
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies11 = [NXOpen.Body.Null] * 1 
    targetBodies11[0] = NXOpen.Body.Null
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies11)
    
    extrudeBuilder5.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder5.Limits.EndExtend.Value.SetFormula("85")
    
    extrudeBuilder5.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies12 = [NXOpen.Body.Null] * 1 
    targetBodies12[0] = body1
    extrudeBuilder5.BooleanOperation.SetTargetBodies(targetBodies12)
    
    extrudeBuilder5.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder5.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder5.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder5.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder4 = extrudeBuilder5.SmartVolumeProfile
    
    smartVolumeProfileBuilder4.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder4.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId62, "拉伸 對話方塊")
    
    section4.DistanceTolerance = 0.01
    
    section4.ChainingTolerance = 0.0094999999999999998
    
    section4.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar3 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    point9 = workPart.Points.CreatePoint(edge1, scalar3, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    direction8 = workPart.Directions.CreateDirection(edge2, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform4 = workPart.Xforms.CreateXformByPlaneXDirPoint(face1, direction8, point9, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem4 = workPart.CoordinateSystems.CreateCoordinateSystem(xform4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder4 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder4.Csys = cartesianCoordinateSystem4
    
    datumCsysBuilder4.DisplayScaleFactor = 1.25
    
    feature7 = datumCsysBuilder4.CommitFeature()
    
    datumCsysBuilder4.Destroy()
    
    markId63 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder4 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder4.Csystem = cartesianCoordinateSystem4
    
    sketchInPlaceBuilder4.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject12 = sketchInPlaceBuilder4.Commit()
    
    sketchInPlaceBuilder4.Destroy()
    
    sketch4 = nXObject12
    sketch4.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId64 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId64, None, True)
    
    markId65 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_002")
    
    markId66 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   對話開始 輪廓
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->曲線(C)->圓(C)...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId66, "Curve")
    
    markId67 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    scaleAboutPoint8 = NXOpen.Point3d(1.6066809550978873, 20.156542891228259, 0.0)
    viewCenter8 = NXOpen.Point3d(-1.6066809550978873, -20.156542891228259, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(1.2853447640783098, 15.891535264968372, 0.0)
    viewCenter9 = NXOpen.Point3d(-1.2853447640783098, -15.891535264968372, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(1.0282758112626478, 12.713228211974696, 0.0)
    viewCenter10 = NXOpen.Point3d(-1.0282758112626478, -12.713228211974696, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint10, viewCenter10)
    
    markId68 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId68, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix3 = theSession.ActiveSketch.Orientation
    
    center3 = NXOpen.Point3d(50.0, 16.0, 7.0)
    arc3 = workPart.Curves.CreateArc(center3, nXMatrix3, 5.0668052433077024, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc3, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_5 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_5.Geometry = arc3
    dimObject1_5.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_5.AssocValue = 0
    dimObject1_5.HelpPoint.X = 0.0
    dimObject1_5.HelpPoint.Y = 0.0
    dimObject1_5.HelpPoint.Z = 0.0
    dimObject1_5.View = NXOpen.NXObject.Null
    dimOrigin5 = NXOpen.Point3d(50.0, 16.0, 8.6958822255899548)
    sketchDimensionalConstraint5 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_5, dimOrigin5, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension5 = sketchDimensionalConstraint5.AssociatedDimension
    
    expression31 = sketchDimensionalConstraint5.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   對話開始 圓
    # ----------------------------------------------
    markId69 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId69, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix4 = theSession.ActiveSketch.Orientation
    
    center4 = NXOpen.Point3d(50.0, 86.411391498505537, 7.0)
    arc4 = workPart.Curves.CreateArc(center4, nXMatrix4, 4.6365891126025218, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc4, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_6 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_6.Geometry = arc4
    dimObject1_6.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_6.AssocValue = 0
    dimObject1_6.HelpPoint.X = 0.0
    dimObject1_6.HelpPoint.Y = 0.0
    dimObject1_6.HelpPoint.Z = 0.0
    dimObject1_6.View = NXOpen.NXObject.Null
    dimOrigin6 = NXOpen.Point3d(50.0, 86.411391498505537, 8.6958822255899548)
    sketchDimensionalConstraint6 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_6, dimOrigin6, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension6 = sketchDimensionalConstraint6.AssociatedDimension
    
    expression32 = sketchDimensionalConstraint6.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   對話開始 圓
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->尺寸(M)->快速(P)...
    # ----------------------------------------------
    markId70 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder3 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines9 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBefore(lines9)
    
    lines10 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAfter(lines10)
    
    lines11 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAbove(lines11)
    
    lines12 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBelow(lines12)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder3.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines13 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBefore(lines13)
    
    lines14 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAfter(lines14)
    
    lines15 = []
    sketchRapidDimensionBuilder3.AppendedText.SetAbove(lines15)
    
    lines16 = []
    sketchRapidDimensionBuilder3.AppendedText.SetBelow(lines16)
    
    theSession.SetUndoMarkName(markId70, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder3.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits77 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits78 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits79 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits80 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits81 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits82 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits83 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits84 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits85 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits86 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder3.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits87 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits88 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits89 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits90 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits91 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits92 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits93 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits94 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits95 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits96 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    convertToFromReferenceBuilder6 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList6 = convertToFromReferenceBuilder6.InputObjects
    
    diameterDimension2 = dimension5
    added6 = selectNXObjectList6.Add(diameterDimension2)
    
    convertToFromReferenceBuilder6.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject13 = convertToFromReferenceBuilder6.Commit()
    
    convertToFromReferenceBuilder6.Destroy()
    
    expression33 = workPart.Expressions.FindObject("p26")
    expression33.SetFormula("10")
    
    markId71 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.Scale(0.98681511522508059)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId71, None)
    
    markId72 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId70, "Edit Driving Value")
    
    convertToFromReferenceBuilder7 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList7 = convertToFromReferenceBuilder7.InputObjects
    
    diameterDimension3 = dimension6
    added7 = selectNXObjectList7.Add(diameterDimension3)
    
    convertToFromReferenceBuilder7.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject14 = convertToFromReferenceBuilder7.Commit()
    
    convertToFromReferenceBuilder7.Destroy()
    
    expression34 = workPart.Expressions.FindObject("p27")
    expression34.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId72, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId73 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId73, None)
    
    markId74 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId72, "Edit Driving Value")
    
    point1_11 = NXOpen.Point3d(50.0, 85.272067258357296, 6.9077058065755637)
    point2_11 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc4, workPart.ModelingViews.WorkView, point1_11, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_11)
    
    point1_12 = NXOpen.Point3d(50.0, 85.272067258357296, 6.9077058065755637)
    point2_12 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc4, workPart.ModelingViews.WorkView, point1_12, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_12)
    
    point1_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_13 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_13, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_13)
    
    dimensionlinearunits97 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits98 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits99 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits100 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits101 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits102 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    edge3 = extrude2.FindObject("EDGE * 130 * 160 {(50,100,0)(50,100,15)(50,100,30) EXTRUDE(1)}")
    point10 = NXOpen.Point3d(50.0, 100.0, 7.8078851941557819)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(edge3, workPart.ModelingViews.WorkView, point10)
    
    point1_14 = NXOpen.Point3d(50.0, 100.0, 7.8078851941557819)
    point2_14 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge3, workPart.ModelingViews.WorkView, point1_14, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_14)
    
    point1_15 = NXOpen.Point3d(50.0, 85.272067258357296, 6.9077058065755637)
    point2_15 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc4, workPart.ModelingViews.WorkView, point1_15, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_15)
    
    point1_16 = NXOpen.Point3d(50.0, 100.0, 7.8078851941557819)
    point2_16 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge3, workPart.ModelingViews.WorkView, point1_16, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_16)
    
    point1_17 = NXOpen.Point3d(50.0, 85.272067258357296, 6.9077058065755637)
    point2_17 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder3.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc4, workPart.ModelingViews.WorkView, point1_17, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_17)
    
    dimensionlinearunits103 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits104 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits105 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits106 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits107 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits108 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits109 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits110 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits111 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits112 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits113 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits114 = sketchRapidDimensionBuilder3.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin1 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin1.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin1.View = NXOpen.View.Null
    assocOrigin1.ViewOfGeometry = workPart.ModelingViews.WorkView
    point11 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin1.PointOnGeometry = point11
    assocOrigin1.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.DimensionLine = 0
    assocOrigin1.AssociatedView = NXOpen.View.Null
    assocOrigin1.AssociatedPoint = NXOpen.Point.Null
    assocOrigin1.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin1.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin1.XOffsetFactor = 0.0
    assocOrigin1.YOffsetFactor = 0.0
    assocOrigin1.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder3.Origin.SetAssociativeOrigin(assocOrigin1)
    
    point12 = NXOpen.Point3d(50.0, 97.030676240272626, -13.131549507920182)
    sketchRapidDimensionBuilder3.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point12)
    
    sketchRapidDimensionBuilder3.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder3.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder3.Style.DimensionStyle.TextCentered = False
    
    markId75 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject15 = sketchRapidDimensionBuilder3.Commit()
    
    theSession.DeleteUndoMark(markId75, None)
    
    theSession.SetUndoMarkName(markId74, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId74, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder3.Destroy()
    
    markId76 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder4 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines17 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBefore(lines17)
    
    lines18 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAfter(lines18)
    
    lines19 = []
    sketchRapidDimensionBuilder4.AppendedText.SetAbove(lines19)
    
    lines20 = []
    sketchRapidDimensionBuilder4.AppendedText.SetBelow(lines20)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder4.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId76, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder4.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits115 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits116 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits117 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits118 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits119 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits120 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits121 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits122 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits123 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits124 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder4.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder4.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder4.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits125 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits126 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits127 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits128 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits129 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits130 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits131 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits132 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits133 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits134 = sketchRapidDimensionBuilder4.Style.UnitsStyle.DimensionLinearUnits
    
    expression35 = workPart.Expressions.FindObject("p28")
    expression35.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId76, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId77 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId77, None)
    
    markId78 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId76, "Edit Driving Value")
    
    perpendicularDimension5 = theSession.ActiveSketch.FindObject("ENTITY 26 3 1")
    point13 = NXOpen.Point3d(50.0, 84.060941782961237, 3.6199982537405919)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(perpendicularDimension5, workPart.ModelingViews.WorkView, point13)
    
    line8 = theSession.ActiveSketch.FindObject("Curve DATUM3")
    point1_18 = NXOpen.Point3d(50.0, 14.2875, 0.0)
    point2_18 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line8, NXOpen.View.Null, point1_18, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_18)
    
    point1_19 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_19 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_19, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_19)
    
    sketchRapidDimensionBuilder4.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    convertToFromReferenceBuilder8 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList8 = convertToFromReferenceBuilder8.InputObjects
    
    added8 = selectNXObjectList8.Add(perpendicularDimension5)
    
    convertToFromReferenceBuilder8.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject16 = convertToFromReferenceBuilder8.Commit()
    
    convertToFromReferenceBuilder8.Destroy()
    
    expression36 = workPart.Expressions.FindObject("p29")
    expression36.SetFormula("6")
    
    theSession.SetUndoMarkVisibility(markId78, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId79 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId79, None)
    
    markId80 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId78, "Edit Driving Value")
    
    perpendicularDimension6 = theSession.ActiveSketch.FindObject("ENTITY 26 5 1")
    point14 = NXOpen.Point3d(50.0, 9.8499836265625245, 3.3208634722823573)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(perpendicularDimension6, workPart.ModelingViews.WorkView, point14)
    
    point1_20 = NXOpen.Point3d(50.0, 14.2875, 0.0)
    point2_20 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line8, NXOpen.View.Null, point1_20, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_20)
    
    point1_21 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_21 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_21, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_21)
    
    sketchRapidDimensionBuilder4.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    convertToFromReferenceBuilder9 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList9 = convertToFromReferenceBuilder9.InputObjects
    
    added9 = selectNXObjectList9.Add(perpendicularDimension6)
    
    convertToFromReferenceBuilder9.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject17 = convertToFromReferenceBuilder9.Commit()
    
    convertToFromReferenceBuilder9.Destroy()
    
    expression37 = workPart.Expressions.FindObject("p30")
    expression37.SetFormula("6")
    
    theSession.SetUndoMarkVisibility(markId80, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId81 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId81, None)
    
    markId82 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId80, "Edit Driving Value")
    
    perpendicularDimension7 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    point15 = NXOpen.Point3d(100.0, 6.6919722398877663, 10.350530836550721)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(perpendicularDimension7, workPart.ModelingViews.WorkView, point15)
    
    line9 = theSession.ActiveSketch.FindObject("Curve DATUM5")
    point1_22 = NXOpen.Point3d(50.0, 0.0, 14.2875)
    point2_22 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line9, NXOpen.View.Null, point1_22, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_22)
    
    point1_23 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_23 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder4.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_23, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_23)
    
    sketchRapidDimensionBuilder4.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    convertToFromReferenceBuilder10 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList10 = convertToFromReferenceBuilder10.InputObjects
    
    added10 = selectNXObjectList10.Add(perpendicularDimension7)
    
    convertToFromReferenceBuilder10.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject18 = convertToFromReferenceBuilder10.Commit()
    
    convertToFromReferenceBuilder10.Destroy()
    
    expression38 = workPart.Expressions.FindObject("p31")
    expression38.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId82, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId83 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId83, None)
    
    markId84 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId82, "Edit Driving Value")
    
    sketchRapidDimensionBuilder4.Destroy()
    
    theSession.UndoToMark(markId84, None)
    
    theSession.DeleteUndoMark(markId84, None)
    
    sketchRapidDimensionBuilder4.Destroy()
    
    # ----------------------------------------------
    #   功能表：任務(K)->完成草圖(K)
    # ----------------------------------------------
    theSession.Preferences.Sketch.SectionView = False
    
    markId85 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId63, None)
    
    section4.DistanceTolerance = 0.01
    
    section4.ChainingTolerance = 0.0094999999999999998
    
    markId86 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves4 = [NXOpen.ICurve.Null] * 2 
    curves4[0] = arc4
    curves4[1] = arc3
    seedPoint4 = NXOpen.Point3d(50.0, 91.666666666666657, 6.0000000000000053)
    regionBoundaryRule4 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch4, curves4, seedPoint4, 0.01)
    
    curves5 = [NXOpen.ICurve.Null] * 2 
    curves5[0] = arc4
    curves5[1] = arc3
    seedPoint5 = NXOpen.Point3d(50.0, 10.000000000000009, 7.6666666666666661)
    regionBoundaryRule5 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch4, curves5, seedPoint5, 0.01)
    
    section4.AllowSelfIntersection(True)
    
    rules4 = [None] * 2 
    rules4[0] = regionBoundaryRule4
    rules4[1] = regionBoundaryRule5
    helpPoint4 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section4.AddToSection(rules4, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint4, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId86, None)
    
    expression39 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression40 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs4 = section4.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression39)
    
    workPart.Expressions.Delete(expression40)
    
    expression41 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression42 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction9 = workPart.Directions.CreateDirection(sketch4, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder5.Direction = direction9
    
    direction10 = extrudeBuilder5.Direction
    
    success2 = direction10.ReverseDirection()
    
    extrudeBuilder5.Direction = direction10
    
    extrudeBuilder5.Limits.EndExtend.Value.SetFormula("40")
    
    extrudeBuilder5.Limits.EndExtend.Value.SetFormula("20")
    
    markId87 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId87, None)
    
    markId88 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder5.ParentFeatureInternal = True
    
    feature8 = extrudeBuilder5.CommitFeature()
    
    theSession.DeleteUndoMark(markId88, None)
    
    theSession.SetUndoMarkName(markId62, "拉伸")
    
    expression43 = extrudeBuilder5.Limits.StartExtend.Value
    expression44 = extrudeBuilder5.Limits.EndExtend.Value
    extrudeBuilder5.Destroy()
    
    workPart.Expressions.Delete(expression30)
    
    workPart.Expressions.Delete(expression41)
    
    workPart.Expressions.Delete(expression42)
    
    rotMatrix7 = NXOpen.Matrix3x3()
    
    rotMatrix7.Xx = 0.71419925386744532
    rotMatrix7.Xy = -0.69867327583408279
    rotMatrix7.Xz = 0.042131691284043704
    rotMatrix7.Yx = -0.23704823588318474
    rotMatrix7.Yy = -0.18480195941937608
    rotMatrix7.Yz = 0.95375907317279529
    rotMatrix7.Zx = -0.65857995690717253
    rotMatrix7.Zy = -0.69116126152297375
    rotMatrix7.Zz = -0.29760468902575565
    translation7 = NXOpen.Point3d(69.705068011529136, 17.019912400641012, 51.637408026999587)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation7, 0.90572327300951838)
    
    rotMatrix8 = NXOpen.Matrix3x3()
    
    rotMatrix8.Xx = 0.12183080986742156
    rotMatrix8.Xy = -0.98129714646003474
    rotMatrix8.Xz = -0.1490408135929138
    rotMatrix8.Yx = -0.25263736568781675
    rotMatrix8.Yy = -0.17587213091640116
    rotMatrix8.Yz = 0.95144277548638967
    rotMatrix8.Zx = -0.95986020608490985
    rotMatrix8.Zy = -0.078261765353931909
    rotMatrix8.Zz = -0.26933897018128938
    translation8 = NXOpen.Point3d(101.51306021598171, 16.997893685904153, 28.10045366532394)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation8, 0.90572327300951838)
    
    # ----------------------------------------------
    #   功能表：插入(S)->設計特徵(E)->拉伸(X)...
    # ----------------------------------------------
    markId89 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    extrudeBuilder6 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section5 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder6.Section = section5
    
    extrudeBuilder6.AllowSelfIntersectingSection(True)
    
    expression45 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit1)
    
    extrudeBuilder6.DistanceTolerance = 0.01
    
    extrudeBuilder6.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies13 = [NXOpen.Body.Null] * 1 
    targetBodies13[0] = NXOpen.Body.Null
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies13)
    
    extrudeBuilder6.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder6.Limits.EndExtend.Value.SetFormula("20")
    
    extrudeBuilder6.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Subtract
    
    targetBodies14 = [NXOpen.Body.Null] * 1 
    targetBodies14[0] = body1
    extrudeBuilder6.BooleanOperation.SetTargetBodies(targetBodies14)
    
    extrudeBuilder6.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder6.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder6.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder6.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder5 = extrudeBuilder6.SmartVolumeProfile
    
    smartVolumeProfileBuilder5.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder5.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId89, "拉伸 對話方塊")
    
    section5.DistanceTolerance = 0.01
    
    section5.ChainingTolerance = 0.0094999999999999998
    
    section5.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    scalar4 = workPart.Scalars.CreateScalar(1.0, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge4 = extrude2.FindObject("EDGE * 120 * 140 {(0,-0,30)(0,-0,15)(0,0,0) EXTRUDE(1)}")
    point16 = workPart.Points.CreatePoint(edge4, scalar4, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    edge5 = extrude2.FindObject("EDGE * 120 * 170 {(0,100,30)(0,50,30)(0,0,30) EXTRUDE(1)}")
    direction11 = workPart.Directions.CreateDirection(edge5, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    face2 = extrude2.FindObject("FACE 120 {(0,50,15) EXTRUDE(1)}")
    xform5 = workPart.Xforms.CreateXformByPlaneXDirPoint(face2, direction11, point16, NXOpen.SmartObject.UpdateOption.WithinModeling, 0.625, False, False)
    
    cartesianCoordinateSystem5 = workPart.CoordinateSystems.CreateCoordinateSystem(xform5, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    datumCsysBuilder5 = workPart.Features.CreateDatumCsysBuilder(NXOpen.Features.Feature.Null)
    
    datumCsysBuilder5.Csys = cartesianCoordinateSystem5
    
    datumCsysBuilder5.DisplayScaleFactor = 1.25
    
    feature9 = datumCsysBuilder5.CommitFeature()
    
    datumCsysBuilder5.Destroy()
    
    markId90 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    theSession.BeginTaskEnvironment()
    
    sketchInPlaceBuilder5 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    sketchInPlaceBuilder5.Csystem = cartesianCoordinateSystem5
    
    sketchInPlaceBuilder5.PlaneOption = NXOpen.Sketch.PlaneOption.Inferred
    
    theSession.Preferences.Sketch.CreateInferredConstraints = True
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = True
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = True
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    nXObject19 = sketchInPlaceBuilder5.Commit()
    
    sketchInPlaceBuilder5.Destroy()
    
    sketch5 = nXObject19
    sketch5.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    markId91 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.DeleteUndoMarksUpToMark(markId91, None, True)
    
    markId92 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_003")
    
    markId93 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    # ----------------------------------------------
    #   對話開始 輪廓
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->曲線(C)->圓(C)...
    # ----------------------------------------------
    theSession.DeleteUndoMark(markId93, "Curve")
    
    markId94 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId95 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    scaleAboutPoint11 = NXOpen.Point3d(-82.817100140046563, 11.392828590694242, 0.0)
    viewCenter11 = NXOpen.Point3d(82.817100140046563, -11.392828590694242, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-66.25368011203723, 9.1142628725553934, 0.0)
    viewCenter12 = NXOpen.Point3d(66.253680112037244, -9.1142628725553934, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(-53.002944089629764, 7.2914102980443145, 0.0)
    viewCenter13 = NXOpen.Point3d(53.002944089629828, -7.2914102980443145, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint13, viewCenter13)
    
    theSession.SetUndoMarkVisibility(markId95, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix5 = theSession.ActiveSketch.Orientation
    
    center5 = NXOpen.Point3d(0.0, 89.0, 11.0)
    arc5 = workPart.Curves.CreateArc(center5, nXMatrix5, 4.2409811251426461, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc5, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_7 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_7.Geometry = arc5
    dimObject1_7.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_7.AssocValue = 0
    dimObject1_7.HelpPoint.X = 0.0
    dimObject1_7.HelpPoint.Y = 0.0
    dimObject1_7.HelpPoint.Z = 0.0
    dimObject1_7.View = NXOpen.NXObject.Null
    dimOrigin7 = NXOpen.Point3d(0.0, 89.0, 12.695882225589955)
    sketchDimensionalConstraint7 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_7, dimOrigin7, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension7 = sketchDimensionalConstraint7.AssociatedDimension
    
    expression46 = sketchDimensionalConstraint7.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   對話開始 圓
    # ----------------------------------------------
    markId96 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId96, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix6 = theSession.ActiveSketch.Orientation
    
    center6 = NXOpen.Point3d(0.0, 14.016100404654043, 11.0)
    arc6 = workPart.Curves.CreateArc(center6, nXMatrix6, 6.281830410622792, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc6, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    dimObject1_8 = NXOpen.Sketch.DimensionGeometry()
    
    dimObject1_8.Geometry = arc6
    dimObject1_8.AssocType = NXOpen.Sketch.AssocType.NotSet
    dimObject1_8.AssocValue = 0
    dimObject1_8.HelpPoint.X = 0.0
    dimObject1_8.HelpPoint.Y = 0.0
    dimObject1_8.HelpPoint.Z = 0.0
    dimObject1_8.View = NXOpen.NXObject.Null
    dimOrigin8 = NXOpen.Point3d(0.0, 14.016100404654043, 12.695882225589955)
    sketchDimensionalConstraint8 = theSession.ActiveSketch.CreateDiameterDimension(dimObject1_8, dimOrigin8, NXOpen.Expression.Null, NXOpen.Sketch.DimensionOption.CreateAsAutomatic)
    
    dimension8 = sketchDimensionalConstraint8.AssociatedDimension
    
    expression47 = sketchDimensionalConstraint8.AssociatedExpression
    
    theSession.ActiveSketch.Update()
    
    # ----------------------------------------------
    #   對話開始 圓
    # ----------------------------------------------
    # ----------------------------------------------
    #   功能表：插入(S)->尺寸(M)->快速(P)...
    # ----------------------------------------------
    markId97 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder5 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines21 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBefore(lines21)
    
    lines22 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAfter(lines22)
    
    lines23 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAbove(lines23)
    
    lines24 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBelow(lines24)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder5.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines25 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBefore(lines25)
    
    lines26 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAfter(lines26)
    
    lines27 = []
    sketchRapidDimensionBuilder5.AppendedText.SetAbove(lines27)
    
    lines28 = []
    sketchRapidDimensionBuilder5.AppendedText.SetBelow(lines28)
    
    theSession.SetUndoMarkName(markId97, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder5.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits135 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits136 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits137 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits138 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits139 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits140 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits141 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits142 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits143 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits144 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder5.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits145 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits146 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits147 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits148 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits149 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits150 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits151 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits152 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits153 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits154 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    convertToFromReferenceBuilder11 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList11 = convertToFromReferenceBuilder11.InputObjects
    
    diameterDimension4 = dimension7
    added11 = selectNXObjectList11.Add(diameterDimension4)
    
    convertToFromReferenceBuilder11.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject20 = convertToFromReferenceBuilder11.Commit()
    
    convertToFromReferenceBuilder11.Destroy()
    
    expression48 = workPart.Expressions.FindObject("p39")
    expression48.SetFormula("10")
    
    markId98 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.Scale(1.1789724718072281)
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId98, None)
    
    markId99 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId97, "Edit Driving Value")
    
    convertToFromReferenceBuilder12 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList12 = convertToFromReferenceBuilder12.InputObjects
    
    diameterDimension5 = dimension8
    added12 = selectNXObjectList12.Add(diameterDimension5)
    
    convertToFromReferenceBuilder12.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject21 = convertToFromReferenceBuilder12.Commit()
    
    convertToFromReferenceBuilder12.Destroy()
    
    expression49 = workPart.Expressions.FindObject("p40")
    expression49.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId99, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId100 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId100, None)
    
    markId101 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId99, "Edit Driving Value")
    
    perpendicularDimension8 = theSession.ActiveSketch.FindObject("ENTITY 26 1 1")
    point17 = NXOpen.Point3d(0.0, 9.7375972093395262, 9.7475872926739928)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(perpendicularDimension8, workPart.ModelingViews.WorkView, point17)
    
    line10 = theSession.ActiveSketch.FindObject("Curve DATUM6")
    point1_24 = NXOpen.Point3d(0.0, -14.2875, -1.4870916997811177e-15)
    point2_24 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line10, NXOpen.View.Null, point1_24, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_24)
    
    point1_25 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_25 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_25, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_25)
    
    sketchRapidDimensionBuilder5.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    convertToFromReferenceBuilder13 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList13 = convertToFromReferenceBuilder13.InputObjects
    
    added13 = selectNXObjectList13.Add(perpendicularDimension8)
    
    convertToFromReferenceBuilder13.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject22 = convertToFromReferenceBuilder13.Commit()
    
    convertToFromReferenceBuilder13.Destroy()
    
    expression50 = workPart.Expressions.FindObject("p41")
    expression50.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId101, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId102 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId102, None)
    
    markId103 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId101, "Edit Driving Value")
    
    point1_26 = NXOpen.Point3d(0.0, 16.524596539173267, 10.000000000000002)
    point2_26 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc6, workPart.ModelingViews.WorkView, point1_26, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_26)
    
    point1_27 = NXOpen.Point3d(0.0, 16.524596539173267, 10.000000000000002)
    point2_27 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc6, workPart.ModelingViews.WorkView, point1_27, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_27)
    
    point1_28 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_28 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_28, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_28)
    
    dimensionlinearunits155 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits156 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits157 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits158 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits159 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits160 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    point18 = NXOpen.Point3d(0.0, -2.2769498823078304e-16, 22.311248113919575)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(edge4, workPart.ModelingViews.WorkView, point18)
    
    point1_29 = NXOpen.Point3d(0.0, -2.2769498823078304e-16, 22.311248113919575)
    point2_29 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge4, workPart.ModelingViews.WorkView, point1_29, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_29)
    
    point1_30 = NXOpen.Point3d(0.0, 16.524596539173267, 10.000000000000002)
    point2_30 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc6, workPart.ModelingViews.WorkView, point1_30, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_30)
    
    point1_31 = NXOpen.Point3d(0.0, -2.2769498823078304e-16, 22.311248113919575)
    point2_31 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge4, workPart.ModelingViews.WorkView, point1_31, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_31)
    
    point1_32 = NXOpen.Point3d(0.0, 16.524596539173267, 10.000000000000002)
    point2_32 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder5.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc6, workPart.ModelingViews.WorkView, point1_32, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_32)
    
    dimensionlinearunits161 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits162 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits163 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits164 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits165 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits166 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits167 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits168 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits169 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits170 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits171 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits172 = sketchRapidDimensionBuilder5.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin2 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin2.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin2.View = NXOpen.View.Null
    assocOrigin2.ViewOfGeometry = workPart.ModelingViews.WorkView
    point19 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin2.PointOnGeometry = point19
    assocOrigin2.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.DimensionLine = 0
    assocOrigin2.AssociatedView = NXOpen.View.Null
    assocOrigin2.AssociatedPoint = NXOpen.Point.Null
    assocOrigin2.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin2.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin2.XOffsetFactor = 0.0
    assocOrigin2.YOffsetFactor = 0.0
    assocOrigin2.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder5.Origin.SetAssociativeOrigin(assocOrigin2)
    
    point20 = NXOpen.Point3d(0.0, -3.1841495291940944, 42.951548034537318)
    sketchRapidDimensionBuilder5.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point20)
    
    sketchRapidDimensionBuilder5.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder5.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Left
    
    sketchRapidDimensionBuilder5.Style.DimensionStyle.TextCentered = False
    
    markId104 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject23 = sketchRapidDimensionBuilder5.Commit()
    
    theSession.DeleteUndoMark(markId104, None)
    
    theSession.SetUndoMarkName(markId103, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId103, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder5.Destroy()
    
    markId105 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder6 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines29 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBefore(lines29)
    
    lines30 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAfter(lines30)
    
    lines31 = []
    sketchRapidDimensionBuilder6.AppendedText.SetAbove(lines31)
    
    lines32 = []
    sketchRapidDimensionBuilder6.AppendedText.SetBelow(lines32)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder6.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId105, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder6.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits173 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits174 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits175 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits176 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits177 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits178 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits179 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits180 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits181 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits182 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder6.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder6.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder6.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits183 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits184 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits185 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits186 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits187 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits188 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits189 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits190 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits191 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits192 = sketchRapidDimensionBuilder6.Style.UnitsStyle.DimensionLinearUnits
    
    expression51 = workPart.Expressions.FindObject("p42")
    expression51.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId105, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId106 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId106, None)
    
    markId107 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId105, "Edit Driving Value")
    
    sketchRapidDimensionBuilder6.Destroy()
    
    theSession.UndoToMark(markId107, None)
    
    theSession.DeleteUndoMark(markId107, None)
    
    sketchRapidDimensionBuilder6.Destroy()
    
    markId108 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId109 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Sketch Drag")
    
    theSession.SetUndoMarkVisibility(markId109, "Sketch Drag", NXOpen.Session.MarkVisibility.Visible)
    
    perpendicularDimension9 = theSession.ActiveSketch.FindObject("ENTITY 26 4 1")
    theSession.UpdateManager.LogForUpdate(perpendicularDimension9)
    
    perpendicularDimension10 = theSession.ActiveSketch.FindObject("ENTITY 26 5 1")
    theSession.UpdateManager.LogForUpdate(perpendicularDimension10)
    
    center7 = NXOpen.Point3d(0.0, 86.855419689732571, 15.0)
    arc5.SetParameters(5.0, center7, 0.0, ( 360.0 * math.pi/180.0 ))
    
    sketchHelpedDimensionalConstraint3 = theSession.ActiveSketch.FindObject("ENTITY 243 11 1")
    sketchHelpedDimensionalConstraint3.Refresh()
    
    sketchHelpedDimensionalConstraint4 = theSession.ActiveSketch.FindObject("ENTITY 243 10 1")
    sketchHelpedDimensionalConstraint4.Refresh()
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId109)
    
    geoms3 = [NXOpen.SmartObject.Null] * 1 
    geoms3[0] = arc5
    theSession.ActiveSketch.UpdateGeometryDisplay(geoms3)
    
    geoms4 = [NXOpen.SmartObject.Null] * 1 
    geoms4[0] = arc5
    theSession.ActiveSketch.UpdateConstraintDisplay(geoms4)
    
    geoms5 = [NXOpen.SmartObject.Null] * 1 
    geoms5[0] = arc5
    theSession.ActiveSketch.UpdateDimensionDisplay(geoms5)
    
    # ----------------------------------------------
    #   功能表：插入(S)->尺寸(M)->快速(P)...
    # ----------------------------------------------
    markId110 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    sketchRapidDimensionBuilder7 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines33 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBefore(lines33)
    
    lines34 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAfter(lines34)
    
    lines35 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAbove(lines35)
    
    lines36 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBelow(lines36)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder7.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    lines37 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBefore(lines37)
    
    lines38 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAfter(lines38)
    
    lines39 = []
    sketchRapidDimensionBuilder7.AppendedText.SetAbove(lines39)
    
    lines40 = []
    sketchRapidDimensionBuilder7.AppendedText.SetBelow(lines40)
    
    theSession.SetUndoMarkName(markId110, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder7.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits193 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits194 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits195 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits196 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits197 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits198 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits199 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits200 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits201 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits202 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder7.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits203 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits204 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits205 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits206 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits207 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits208 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits209 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits210 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits211 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits212 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    point1_33 = NXOpen.Point3d(0.0, 86.855419689732571, 15.0)
    point2_33 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc5, workPart.ModelingViews.WorkView, point1_33, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_33)
    
    point1_34 = NXOpen.Point3d(0.0, 86.855419689732571, 15.0)
    point2_34 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, arc5, workPart.ModelingViews.WorkView, point1_34, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_34)
    
    point1_35 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_35 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_35, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_35)
    
    dimensionlinearunits213 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits214 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits215 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits216 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits217 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits218 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    edge6 = extrude2.FindObject("EDGE * 120 * 160 {(0,100,0)(0,100,15)(0,100,30) EXTRUDE(1)}")
    point21 = NXOpen.Point3d(0.0, 100.00000000000001, 20.21730464371198)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(edge6, workPart.ModelingViews.WorkView, point21)
    
    point1_36 = NXOpen.Point3d(0.0, 100.00000000000001, 20.21730464371198)
    point2_36 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge6, workPart.ModelingViews.WorkView, point1_36, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_36)
    
    point1_37 = NXOpen.Point3d(0.0, 86.855419689732571, 15.0)
    point2_37 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc5, workPart.ModelingViews.WorkView, point1_37, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_37)
    
    point1_38 = NXOpen.Point3d(0.0, 100.00000000000001, 20.21730464371198)
    point2_38 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, edge6, workPart.ModelingViews.WorkView, point1_38, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_38)
    
    point1_39 = NXOpen.Point3d(0.0, 86.855419689732571, 15.0)
    point2_39 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder7.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.Center, arc5, workPart.ModelingViews.WorkView, point1_39, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_39)
    
    dimensionlinearunits219 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits220 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits221 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits222 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits223 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits224 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits225 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits226 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits227 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits228 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits229 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits230 = sketchRapidDimensionBuilder7.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometryFromLeader(True)
    
    assocOrigin3 = NXOpen.Annotations.Annotation.AssociativeOriginData()
    
    assocOrigin3.OriginType = NXOpen.Annotations.AssociativeOriginType.RelativeToGeometry
    assocOrigin3.View = NXOpen.View.Null
    assocOrigin3.ViewOfGeometry = workPart.ModelingViews.WorkView
    point22 = workPart.Points.FindObject("ENTITY 2 2")
    assocOrigin3.PointOnGeometry = point22
    assocOrigin3.VertAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.VertAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.HorizAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.HorizAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.AlignedAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.DimensionLine = 0
    assocOrigin3.AssociatedView = NXOpen.View.Null
    assocOrigin3.AssociatedPoint = NXOpen.Point.Null
    assocOrigin3.OffsetAnnotation = NXOpen.Annotations.Annotation.Null
    assocOrigin3.OffsetAlignmentPosition = NXOpen.Annotations.AlignmentPosition.TopLeft
    assocOrigin3.XOffsetFactor = 0.0
    assocOrigin3.YOffsetFactor = 0.0
    assocOrigin3.StackAlignmentPosition = NXOpen.Annotations.StackAlignmentPosition.Above
    sketchRapidDimensionBuilder7.Origin.SetAssociativeOrigin(assocOrigin3)
    
    point23 = NXOpen.Point3d(0.0, 95.231193570562965, 41.007171955058837)
    sketchRapidDimensionBuilder7.Origin.Origin.SetValue(NXOpen.TaggedObject.Null, NXOpen.View.Null, point23)
    
    sketchRapidDimensionBuilder7.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder7.Style.LineArrowStyle.LeaderOrientation = NXOpen.Annotations.LeaderSide.Right
    
    sketchRapidDimensionBuilder7.Style.DimensionStyle.TextCentered = False
    
    markId111 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    nXObject24 = sketchRapidDimensionBuilder7.Commit()
    
    theSession.DeleteUndoMark(markId111, None)
    
    theSession.SetUndoMarkName(markId110, "快速尺寸")
    
    theSession.SetUndoMarkVisibility(markId110, None, NXOpen.Session.MarkVisibility.Visible)
    
    sketchRapidDimensionBuilder7.Destroy()
    
    markId112 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    sketchRapidDimensionBuilder8 = workPart.Sketches.CreateRapidDimensionBuilder()
    
    lines41 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBefore(lines41)
    
    lines42 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAfter(lines42)
    
    lines43 = []
    sketchRapidDimensionBuilder8.AppendedText.SetAbove(lines43)
    
    lines44 = []
    sketchRapidDimensionBuilder8.AppendedText.SetBelow(lines44)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.Anchor = NXOpen.Annotations.OriginBuilder.AlignmentPosition.MidCenter
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitDeviation = "H"
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.LimitFitShaftDeviation = "g"
    
    sketchRapidDimensionBuilder8.Driving.DrivingMethod = NXOpen.Annotations.DrivingValueBuilder.DrivingValueMethod.Driving
    
    theSession.SetUndoMarkName(markId112, "快速尺寸 對話方塊")
    
    sketchRapidDimensionBuilder8.Origin.Plane.PlaneMethod = NXOpen.Annotations.PlaneBuilder.PlaneMethodType.XyPlane
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    dimensionlinearunits231 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits232 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits233 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits234 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits235 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits236 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits237 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits238 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits239 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits240 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Origin.SetInferRelativeToGeometry(True)
    
    sketchRapidDimensionBuilder8.Measurement.Direction = NXOpen.Direction.Null
    
    sketchRapidDimensionBuilder8.Measurement.DirectionView = NXOpen.View.Null
    
    sketchRapidDimensionBuilder8.Style.DimensionStyle.NarrowDisplayType = NXOpen.Annotations.NarrowDisplayOption.NotSet
    
    dimensionlinearunits241 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits242 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits243 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits244 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits245 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits246 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits247 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits248 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits249 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    dimensionlinearunits250 = sketchRapidDimensionBuilder8.Style.UnitsStyle.DimensionLinearUnits
    
    expression52 = workPart.Expressions.FindObject("p43")
    expression52.SetFormula("10")
    
    theSession.SetUndoMarkVisibility(markId112, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId113 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId113, None)
    
    markId114 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId112, "Edit Driving Value")
    
    point24 = NXOpen.Point3d(0.0, 84.76147621952498, 9.1493177297575361)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(perpendicularDimension9, workPart.ModelingViews.WorkView, point24)
    
    point1_40 = NXOpen.Point3d(0.0, -14.2875, -1.4870916997811177e-15)
    point2_40 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.FirstAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, line10, NXOpen.View.Null, point1_40, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_40)
    
    point1_41 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2_41 = NXOpen.Point3d(0.0, 0.0, 0.0)
    sketchRapidDimensionBuilder8.SecondAssociativity.SetValue(NXOpen.InferSnapType.SnapType.NotSet, NXOpen.TaggedObject.Null, workPart.ModelingViews.WorkView, point1_41, NXOpen.TaggedObject.Null, NXOpen.View.Null, point2_41)
    
    sketchRapidDimensionBuilder8.FirstAssociativity.Value = NXOpen.TaggedObject.Null
    
    convertToFromReferenceBuilder14 = workPart.Sketches.CreateConvertToFromReferenceBuilder()
    
    selectNXObjectList14 = convertToFromReferenceBuilder14.InputObjects
    
    added14 = selectNXObjectList14.Add(perpendicularDimension9)
    
    convertToFromReferenceBuilder14.OutputState = NXOpen.ConvertToFromReferenceBuilder.OutputType.Active
    
    nXObject25 = convertToFromReferenceBuilder14.Commit()
    
    convertToFromReferenceBuilder14.Destroy()
    
    expression53 = workPart.Expressions.FindObject("p44")
    expression53.SetFormula("6")
    
    theSession.SetUndoMarkVisibility(markId114, None, NXOpen.Session.MarkVisibility.Visible)
    
    markId115 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.ActiveSketch.LocalUpdate()
    
    theSession.DeleteUndoMark(markId115, None)
    
    markId116 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "快速尺寸")
    
    theSession.SetUndoMarkName(markId114, "Edit Driving Value")
    
    # ----------------------------------------------
    #   功能表：任務(K)->完成草圖(K)
    # ----------------------------------------------
    sketchRapidDimensionBuilder8.Destroy()
    
    theSession.UndoToMark(markId116, None)
    
    theSession.DeleteUndoMark(markId116, None)
    
    sketchRapidDimensionBuilder8.Destroy()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId117 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.SketchOnly)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    theSession.DeleteUndoMark(markId90, None)
    
    section5.DistanceTolerance = 0.01
    
    section5.ChainingTolerance = 0.0094999999999999998
    
    markId118 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    curves6 = [NXOpen.ICurve.Null] * 2 
    curves6[0] = arc6
    curves6[1] = arc5
    seedPoint6 = NXOpen.Point3d(0.0, 10.000000000000009, 8.3333333333333339)
    regionBoundaryRule6 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch5, curves6, seedPoint6, 0.01)
    
    curves7 = [NXOpen.ICurve.Null] * 2 
    curves7[0] = arc6
    curves7[1] = arc5
    seedPoint7 = NXOpen.Point3d(0.0, 88.333333333333314, 6.0000000000000053)
    regionBoundaryRule7 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch5, curves7, seedPoint7, 0.01)
    
    section5.AllowSelfIntersection(True)
    
    rules5 = [None] * 2 
    rules5[0] = regionBoundaryRule6
    rules5[1] = regionBoundaryRule7
    helpPoint5 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section5.AddToSection(rules5, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint5, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId118, None)
    
    expression54 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression55 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    refs5 = section5.EvaluateAndAskOutputEntities()
    
    workPart.Expressions.Delete(expression54)
    
    workPart.Expressions.Delete(expression55)
    
    expression56 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    expression57 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    direction12 = workPart.Directions.CreateDirection(sketch5, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder6.Direction = direction12
    
    rotMatrix9 = NXOpen.Matrix3x3()
    
    rotMatrix9.Xx = -0.71005698076825463
    rotMatrix9.Xy = -0.67260008731849896
    rotMatrix9.Xz = -0.20839435357373076
    rotMatrix9.Yx = 0.1812141800563386
    rotMatrix9.Yy = -0.46053521226078087
    rotMatrix9.Yz = 0.86894691392191614
    rotMatrix9.Zx = -0.68042670803604699
    rotMatrix9.Zy = 0.57923781023605292
    rotMatrix9.Zz = 0.44889091568460332
    translation9 = NXOpen.Point3d(107.76570512450913, 21.622197032986364, -22.533810853385276)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix9, translation9, 0.90572327300951838)
    
    direction13 = extrudeBuilder6.Direction
    
    success3 = direction13.ReverseDirection()
    
    extrudeBuilder6.Direction = direction13
    
    extrudeBuilder6.Limits.EndExtend.Value.SetFormula("20")
    
    markId119 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    theSession.DeleteUndoMark(markId119, None)
    
    markId120 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "拉伸")
    
    extrudeBuilder6.ParentFeatureInternal = True
    
    feature10 = extrudeBuilder6.CommitFeature()
    
    theSession.DeleteUndoMark(markId120, None)
    
    theSession.SetUndoMarkName(markId89, "拉伸")
    
    expression58 = extrudeBuilder6.Limits.StartExtend.Value
    expression59 = extrudeBuilder6.Limits.EndExtend.Value
    extrudeBuilder6.Destroy()
    
    workPart.Expressions.Delete(expression45)
    
    workPart.Expressions.Delete(expression56)
    
    workPart.Expressions.Delete(expression57)
    
    rotMatrix10 = NXOpen.Matrix3x3()
    
    rotMatrix10.Xx = 0.061657548309723607
    rotMatrix10.Xy = -0.97990162967202055
    rotMatrix10.Xz = -0.18971331767314129
    rotMatrix10.Yx = 0.37509803948709564
    rotMatrix10.Yy = -0.15339232670189012
    rotMatrix10.Yz = 0.91420580553938402
    rotMatrix10.Zx = -0.92493232590788255
    rotMatrix10.Zy = -0.12752878214386207
    rotMatrix10.Zz = 0.35810138538622255
    translation10 = NXOpen.Point3d(103.55770347672683, 0.73907289501089402, 20.279002166882083)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix10, translation10, 0.90572327300951838)
    
    rotMatrix11 = NXOpen.Matrix3x3()
    
    rotMatrix11.Xx = 0.62469785541377498
    rotMatrix11.Xy = -0.77887348181192728
    rotMatrix11.Xz = 0.055755616502623929
    rotMatrix11.Yx = -0.11259199318479546
    rotMatrix11.Yy = -0.019188256423704191
    rotMatrix11.Yz = 0.99345601507368808
    rotMatrix11.Zx = -0.77270669242093193
    rotMatrix11.Zy = -0.62688747805772638
    rotMatrix11.Zz = -0.099681780393004071
    translation11 = NXOpen.Point3d(75.748254393484387, 5.0323670548843111, 48.308043612089939)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix11, translation11, 0.90572327300951838)
    
    # ----------------------------------------------
    #   功能表：檔案(F)->另存新檔(A)...
    # ----------------------------------------------
    partSaveStatus1 = workPart.SaveAs("D:\\calculator2024\\Siemens\\ROBOT\\1")
    
    partSaveStatus1.Dispose()
    # ----------------------------------------------
    #   功能表：工具(T)->動作記錄(J)->停止錄製(S)
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()