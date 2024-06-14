﻿# NX 1872
# Journal created by User on Fri Jun 14 19:56:47 2024 台北標準時間

#
import math
import NXOpen
import NXOpen.Assemblies
import NXOpen.Positioning
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   功能表：組立件(A)->元件位置(P)->組立約束(N)...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "通過定位任務建立約束")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    componentPositioner1 = workPart.ComponentAssembly.Positioner
    
    componentPositioner1.ClearNetwork()
    
    arrangement1 = workPart.ComponentAssembly.Arrangements.FindObject("Arrangement 1")
    componentPositioner1.PrimaryArrangement = arrangement1
    
    componentPositioner1.BeginAssemblyConstraints()
    
    allowInterpartPositioning1 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    unit2 = workPart.UnitCollection.FindObject("Degrees")
    expression4 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression5 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression6 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression7 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression8 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network1 = componentPositioner1.EstablishNetwork()
    
    componentNetwork1 = network1
    componentNetwork1.MoveObjectsState = True
    
    componentNetwork1.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork1.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId2, "組立約束 對話方塊")
    
    componentNetwork1.MoveObjectsState = True
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.024104868203918502
    rotMatrix1.Xy = 0.98928071849113997
    rotMatrix1.Xz = -0.14402296813536922
    rotMatrix1.Yx = -0.097474776670905761
    rotMatrix1.Yy = 0.14570417294403279
    rotMatrix1.Yz = 0.98451458186237728
    rotMatrix1.Zx = 0.99494604036692524
    rotMatrix1.Zy = -0.009692987586151617
    rotMatrix1.Zz = 0.099942096985333365
    translation1 = NXOpen.Point3d(-39.703797122527277, 11.949516498952141, 38.967753002916396)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.87275667986661054)
    
    scaleAboutPoint1 = NXOpen.Point3d(12.429485693910243, 21.221073135944369, 0.0)
    viewCenter1 = NXOpen.Point3d(-12.429485693910243, -21.221073135944369, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    scaleAboutPoint2 = NXOpen.Point3d(8.973482354627933, 16.976858508755495, 0.0)
    viewCenter2 = NXOpen.Point3d(-8.9734823546278513, -16.976858508755495, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint2, viewCenter2)
    
    scaleAboutPoint3 = NXOpen.Point3d(6.5967221634021929, 13.19344432680427, 0.0)
    viewCenter3 = NXOpen.Point3d(-6.5967221634020605, -13.19344432680427, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint3, viewCenter3)
    
    component1 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 1 1")
    face1 = component1.FindObject("PROTO#.Features|EXTRUDE(3)|FACE 170 {(40,10,11) EXTRUDE(1)}")
    line1 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line1.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint1 = componentPositioner1.CreateConstraint(True)
    
    componentConstraint1 = constraint1
    componentConstraint1.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.InferAlign
    
    componentConstraint1.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    component2 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 3 2")
    face2 = component2.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 130 {(40,0,0) EXTRUDE(1)}")
    constraintReference1 = componentConstraint1.CreateConstraintReference(component2, face2, False, False, False)
    
    helpPoint1 = NXOpen.Point3d(11.11535507711084, -140.76828941438845, -0.42148276304487808)
    constraintReference1.HelpPoint = helpPoint1
    
    face3 = component1.FindObject("PROTO#.Features|EXTRUDE(3)|FACE 150 {(30,10,6) EXTRUDE(1)}")
    constraintReference2 = componentConstraint1.CreateConstraintReference(component1, face3, False, False, False)
    
    helpPoint2 = NXOpen.Point3d(33.338913438299862, 43.943120043842079, 4.7170478498514958)
    constraintReference2.HelpPoint = helpPoint2
    
    constraintReference2.SetFixHint(True)
    
    componentConstraint1.SetAlignmentHint(NXOpen.Positioning.Constraint.Alignment.ContraAlign)
    
    objects1 = [NXOpen.TaggedObject.Null] * 1 
    objects1[0] = line1
    nErrs1 = theSession.UpdateManager.AddObjectsToDeleteList(objects1)
    
    componentNetwork1.Solve()
    
    scaleAboutPoint4 = NXOpen.Point3d(-2.949122849520907, -18.470822057525993, 0.0)
    viewCenter4 = NXOpen.Point3d(2.9491228495210131, 18.470822057525993, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint4, viewCenter4)
    
    scaleAboutPoint5 = NXOpen.Point3d(-5.8206372030018354, -23.282548812007541, 0.0)
    viewCenter5 = NXOpen.Point3d(5.8206372030019349, 23.282548812007541, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint5, viewCenter5)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.53267373674540319
    rotMatrix2.Xy = 0.83283380383349148
    rotMatrix2.Xz = 0.15048769176885993
    rotMatrix2.Yx = -0.75782735015180824
    rotMatrix2.Yy = 0.39021454316536586
    rotMatrix2.Yz = 0.52290564891204405
    rotMatrix2.Zx = 0.37677101473384095
    rotMatrix2.Zy = -0.39258179465491544
    rotMatrix2.Zz = 0.83900127351628495
    translation2 = NXOpen.Point3d(-15.388859500422793, -48.588153894332976, -25.944458409838397)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 1.0909458498332634)
    
    scaleAboutPoint6 = NXOpen.Point3d(-38.561721469887445, -42.442146271888767, 0.0)
    viewCenter6 = NXOpen.Point3d(38.561721469887523, 42.442146271888724, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint6, viewCenter6)
    
    scaleAboutPoint7 = NXOpen.Point3d(-30.655355935809922, -33.759695777410968, 0.0)
    viewCenter7 = NXOpen.Point3d(30.655355935809954, 33.759695777410897, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint7, viewCenter7)
    
    scaleAboutPoint8 = NXOpen.Point3d(-24.524284748647922, -27.00775662192877, 0.0)
    viewCenter8 = NXOpen.Point3d(24.524284748647975, 27.007756621928706, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint8, viewCenter8)
    
    scaleAboutPoint9 = NXOpen.Point3d(-19.619427798918338, -21.606205297543038, 0.0)
    viewCenter9 = NXOpen.Point3d(19.61942779891838, 21.606205297542964, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint9, viewCenter9)
    
    scaleAboutPoint10 = NXOpen.Point3d(-24.524284748647929, -27.16297361400882, 0.0)
    viewCenter10 = NXOpen.Point3d(24.524284748648011, 27.162973614008742, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint10, viewCenter10)
    
    scaleAboutPoint11 = NXOpen.Point3d(-30.655355935809901, -33.953717017511046, 0.0)
    viewCenter11 = NXOpen.Point3d(30.655355935809965, 33.953717017510961, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint11, viewCenter11)
    
    scaleAboutPoint12 = NXOpen.Point3d(-38.319194919762388, -42.44214627188876, 0.0)
    viewCenter12 = NXOpen.Point3d(38.319194919762431, 42.442146271888717, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint12, viewCenter12)
    
    scaleAboutPoint13 = NXOpen.Point3d(-47.898993649702966, -53.05268283986095, 0.0)
    viewCenter13 = NXOpen.Point3d(47.898993649703016, 53.0526828398609, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint13, viewCenter13)
    
    scaleAboutPoint14 = NXOpen.Point3d(-84.884292543777448, -104.58957474144015, 0.0)
    viewCenter14 = NXOpen.Point3d(84.884292543777505, 104.58957474144007, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint14, viewCenter14)
    
    scaleAboutPoint15 = NXOpen.Point3d(-106.57905034793477, -130.73696842680016, 0.0)
    viewCenter15 = NXOpen.Point3d(106.57905034793485, 130.73696842680013, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint15, viewCenter15)
    
    scaleAboutPoint16 = NXOpen.Point3d(-138.55276545231519, -163.42121053350019, 0.0)
    viewCenter16 = NXOpen.Point3d(138.55276545231538, 163.4212105335001, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint16, viewCenter16)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId3)
    
    componentNetwork1.Solve()
    
    componentPositioner1.ClearNetwork()
    
    nErrs3 = theSession.UpdateManager.AddToDeleteList(componentNetwork1)
    
    componentPositioner1.DeleteNonPersistentConstraints()
    
    nErrs4 = theSession.UpdateManager.DoUpdate(markId3)
    
    theSession.DeleteUndoMark(markId5, None)
    
    theSession.SetUndoMarkName(markId2, "組立約束")
    
    componentPositioner1.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner1.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner2 = workPart.ComponentAssembly.Positioner
    
    componentPositioner2.ClearNetwork()
    
    componentPositioner2.PrimaryArrangement = arrangement1
    
    componentPositioner2.BeginAssemblyConstraints()
    
    allowInterpartPositioning2 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression9 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression10 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression11 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression12 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression13 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression14 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression15 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression16 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network2 = componentPositioner2.EstablishNetwork()
    
    componentNetwork2 = network2
    componentNetwork2.MoveObjectsState = True
    
    componentNetwork2.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork2.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId6, "組立約束 對話方塊")
    
    componentNetwork2.MoveObjectsState = True
    
    componentNetwork2.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    scaleAboutPoint17 = NXOpen.Point3d(-206.49691004912364, -272.36868422250029, 0.0)
    viewCenter17 = NXOpen.Point3d(206.4969100491239, 272.36868422250029, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint17, viewCenter17)
    
    scaleAboutPoint18 = NXOpen.Point3d(-165.19752803929896, -217.89494737800021, 0.0)
    viewCenter18 = NXOpen.Point3d(165.19752803929904, 217.89494737800024, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint18, viewCenter18)
    
    face4 = component2.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 140 {(20,0,-5.0000000000001) EXTRUDE(1)}")
    line2 = workPart.Lines.CreateFaceAxis(face4, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scaleAboutPoint19 = NXOpen.Point3d(-132.15802243143906, -173.84227323418702, 0.0)
    viewCenter19 = NXOpen.Point3d(132.15802243143926, 173.84227323418705, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint19, viewCenter19)
    
    scaleAboutPoint20 = NXOpen.Point3d(-107.62115661800343, -135.28434124164528, 0.0)
    viewCenter20 = NXOpen.Point3d(107.6211566180037, 135.28434124164539, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint20, viewCenter20)
    
    scaleAboutPoint21 = NXOpen.Point3d(-87.309558045028098, -105.1958911167527, 0.0)
    viewCenter21 = NXOpen.Point3d(87.309558045028311, 105.1958911167528, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint21, viewCenter21)
    
    scaleAboutPoint22 = NXOpen.Point3d(-84.156712893402116, -68.392487135272106, 0.0)
    viewCenter22 = NXOpen.Point3d(84.156712893402329, 68.392487135272177, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint22, viewCenter22)
    
    scaleAboutPoint23 = NXOpen.Point3d(-67.325370314721653, -54.713989708217667, 0.0)
    viewCenter23 = NXOpen.Point3d(67.32537031472188, 54.713989708217717, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint23, viewCenter23)
    
    scaleAboutPoint24 = NXOpen.Point3d(-53.860296251777314, -43.771191766574134, 0.0)
    viewCenter24 = NXOpen.Point3d(53.86029625177752, 43.771191766574198, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint24, viewCenter24)
    
    objects2 = [NXOpen.TaggedObject.Null] * 1 
    objects2[0] = line2
    nErrs5 = theSession.UpdateManager.AddObjectsToDeleteList(objects2)
    
    scaleAboutPoint25 = NXOpen.Point3d(-2.7318190606087698, -22.599594046855298, 0.0)
    viewCenter25 = NXOpen.Point3d(2.7318190606090029, 22.59959404685533, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint25, viewCenter25)
    
    scaleAboutPoint26 = NXOpen.Point3d(-3.2595568336809335, -28.094275566489063, 0.0)
    viewCenter26 = NXOpen.Point3d(3.259556833681172, 28.094275566489092, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint26, viewCenter26)
    
    scaleAboutPoint27 = NXOpen.Point3d(-4.0744460421011999, -35.117844458111342, 0.0)
    viewCenter27 = NXOpen.Point3d(4.0744460421014148, 35.117844458111364, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint27, viewCenter27)
    
    scaleAboutPoint28 = NXOpen.Point3d(-5.0930575526264992, -43.897305572639155, 0.0)
    viewCenter28 = NXOpen.Point3d(5.0930575526267887, 43.897305572639176, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint28, viewCenter28)
    
    scaleAboutPoint29 = NXOpen.Point3d(-6.063163753126819, -53.658999215173566, 0.0)
    viewCenter29 = NXOpen.Point3d(6.063163753127129, 53.658999215173566, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint29, viewCenter29)
    
    scaleAboutPoint30 = NXOpen.Point3d(14.778961648247053, -50.021100963297393, 0.0)
    viewCenter30 = NXOpen.Point3d(-14.77896164824686, 50.021100963297393, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint30, viewCenter30)
    
    scaleAboutPoint31 = NXOpen.Point3d(18.473702060308817, -62.526376204121739, 0.0)
    viewCenter31 = NXOpen.Point3d(-18.473702060308614, 62.526376204121739, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint31, viewCenter31)
    
    scaleAboutPoint32 = NXOpen.Point3d(23.68423341065224, -78.157970255152165, 0.0)
    viewCenter32 = NXOpen.Point3d(-23.684233410652038, 78.157970255152165, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint32, viewCenter32)
    
    scaleAboutPoint33 = NXOpen.Point3d(45.8882022331385, -93.256669054442867, 0.0)
    viewCenter33 = NXOpen.Point3d(-45.8882022331385, 93.256669054442995, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint33, viewCenter33)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = -0.028702653875958731
    rotMatrix3.Xy = 0.9910226017197763
    rotMatrix3.Xz = -0.13057702914769567
    rotMatrix3.Yx = 0.04974190469531134
    rotMatrix3.Yy = 0.1318850832349123
    rotMatrix3.Yz = 0.99001619569449351
    rotMatrix3.Zx = 0.99834958835958432
    rotMatrix3.Zy = 0.021920942057352351
    rotMatrix3.Zz = -0.053080803701140496
    translation3 = NXOpen.Point3d(51.181784899974453, -32.071310588293002, 35.366841193283022)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 0.28598490885869127)
    
    scaleAboutPoint34 = NXOpen.Point3d(61.986079629441186, -27.754961028107939, 0.0)
    viewCenter34 = NXOpen.Point3d(-61.986079629441186, 27.754961028108017, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint34, viewCenter34)
    
    scaleAboutPoint35 = NXOpen.Point3d(46.62833452722154, -23.684233410652158, 0.0)
    viewCenter35 = NXOpen.Point3d(-46.62833452722154, 23.684233410652283, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint35, viewCenter35)
    
    scaleAboutPoint36 = NXOpen.Point3d(37.302667621777232, -18.947386728521728, 0.0)
    viewCenter36 = NXOpen.Point3d(-37.302667621777132, 18.947386728521828, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint36, viewCenter36)
    
    scaleAboutPoint37 = NXOpen.Point3d(29.842134097421823, -15.15790938281738, 0.0)
    viewCenter37 = NXOpen.Point3d(-29.842134097421745, 15.157909382817461, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint37, viewCenter37)
    
    scaleAboutPoint38 = NXOpen.Point3d(48.126362290445243, -10.610536567972124, 0.0)
    viewCenter38 = NXOpen.Point3d(-48.126362290445179, 10.61053656797222, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint38, viewCenter38)
    
    scaleAboutPoint39 = NXOpen.Point3d(45.776886336108596, -6.9726383160959671, 0.0)
    viewCenter39 = NXOpen.Point3d(-45.77688633610844, 6.9726383160960967, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint39, viewCenter39)
    
    scaleAboutPoint40 = NXOpen.Point3d(40.986986971138329, -4.6080044523764334, 0.0)
    viewCenter40 = NXOpen.Point3d(-40.986986971138123, 4.6080044523765569, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint40, viewCenter40)
    
    scaleAboutPoint41 = NXOpen.Point3d(36.281971898711816, -1.9402124010005823, 0.0)
    viewCenter41 = NXOpen.Point3d(-36.281971898711603, 1.9402124010006816, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint41, viewCenter41)
    
    scaleAboutPoint42 = NXOpen.Point3d(30.888181423930085, 2.1730378891207502, 0.0)
    viewCenter42 = NXOpen.Point3d(-30.888181423929861, -2.1730378891206312, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint42, viewCenter42)
    
    scaleAboutPoint43 = NXOpen.Point3d(24.710545139144077, 1.7384303112966002, 0.0)
    viewCenter43 = NXOpen.Point3d(-24.710545139143864, -1.7384303112965047, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint43, viewCenter43)
    
    scaleAboutPoint44 = NXOpen.Point3d(19.768436111315292, 1.3907442490373059, 0.0)
    viewCenter44 = NXOpen.Point3d(-19.768436111315072, -1.3907442490371873, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint44, viewCenter44)
    
    scaleAboutPoint45 = NXOpen.Point3d(15.973691088942221, 1.1920664991748393, 0.0)
    viewCenter45 = NXOpen.Point3d(-15.973691088942019, -1.192066499174731, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint45, viewCenter45)
    
    line3 = workPart.Lines.CreateFaceAxis(face1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint2 = componentPositioner2.CreateConstraint(True)
    
    componentConstraint2 = constraint2
    componentConstraint2.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge1 = component2.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 130 * 140 {(40,-2.5000000000001,4.3301270189223)(40,5.0000000000001,-0)(40,-2.5000000000001,-4.3301270189223) EXTRUDE(1)}")
    constraintReference3 = componentConstraint2.CreateConstraintReference(component2, edge1, False, False, False)
    
    helpPoint3 = NXOpen.Point3d(33.338913438327154, -144.91832604683628, 3.6248526982316478)
    constraintReference3.HelpPoint = helpPoint3
    
    edge2 = component1.FindObject("PROTO#.Features|EXTRUDE(3)|EDGE * 150 * 170 {(30,7.5,1.6698729810778)(30,15,6)(30,7.5,10.3301270189222) EXTRUDE(1)}")
    constraintReference4 = componentConstraint2.CreateConstraintReference(component1, edge2, False, False, False)
    
    helpPoint4 = NXOpen.Point3d(33.33891343832714, 45.56058451428914, 10.942713838463453)
    constraintReference4.HelpPoint = helpPoint4
    
    constraintReference4.SetFixHint(True)
    
    objects3 = [NXOpen.TaggedObject.Null] * 1 
    objects3[0] = line3
    nErrs6 = theSession.UpdateManager.AddObjectsToDeleteList(objects3)
    
    componentNetwork2.Solve()
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.39671593184779702
    rotMatrix4.Xy = 0.91770701222053075
    rotMatrix4.Xz = -0.020743894026906441
    rotMatrix4.Yx = -0.7350273906825836
    rotMatrix4.Yy = 0.33111982389713013
    rotMatrix4.Yz = 0.59168775310013355
    rotMatrix4.Zx = 0.54986471460213238
    rotMatrix4.Zy = -0.21948462803485566
    rotMatrix4.Zz = 0.80590030009419489
    translation4 = NXOpen.Point3d(-7.1733686225202993, -65.844663907801092, 6.2782460232449466)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 4.161628150303895)
    
    scaleAboutPoint46 = NXOpen.Point3d(13.287567910801709, 3.8146127973593726, 0.0)
    viewCenter46 = NXOpen.Point3d(-13.287567910801492, -3.814612797359259, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint46, viewCenter46)
    
    scaleAboutPoint47 = NXOpen.Point3d(16.450517688612148, 4.5298526968642374, 0.0)
    viewCenter47 = NXOpen.Point3d(-16.450517688611939, -4.5298526968641291, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint47, viewCenter47)
    
    scaleAboutPoint48 = NXOpen.Point3d(20.563147110765154, 5.6623158710802883, 0.0)
    viewCenter48 = NXOpen.Point3d(-20.563147110764941, -5.6623158710801702, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint48, viewCenter48)
    
    scaleAboutPoint49 = NXOpen.Point3d(25.579760294792354, 6.9537212451863057, 0.0)
    viewCenter49 = NXOpen.Point3d(-25.579760294792163, -6.9537212451861894, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint49, viewCenter49)
    
    scaleAboutPoint50 = NXOpen.Point3d(32.750785328890686, 2.4834718732808461, 0.0)
    viewCenter50 = NXOpen.Point3d(-32.750785328890466, -2.4834718732807404, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint50, viewCenter50)
    
    scaleAboutPoint51 = NXOpen.Point3d(40.938481661113322, 1.1641274406004256, 0.0)
    viewCenter51 = NXOpen.Point3d(-40.938481661113109, -1.1641274406003261, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint51, viewCenter51)
    
    scaleAboutPoint52 = NXOpen.Point3d(51.173102076391615, -0.9701062005002582, 0.0)
    viewCenter52 = NXOpen.Point3d(-51.173102076391409, 0.97010620050036156, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint52, viewCenter52)
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs7 = theSession.UpdateManager.DoUpdate(markId7)
    
    componentNetwork2.Solve()
    
    componentPositioner2.ClearNetwork()
    
    nErrs8 = theSession.UpdateManager.AddToDeleteList(componentNetwork2)
    
    componentPositioner2.DeleteNonPersistentConstraints()
    
    nErrs9 = theSession.UpdateManager.DoUpdate(markId7)
    
    theSession.DeleteUndoMark(markId9, None)
    
    theSession.SetUndoMarkName(markId6, "組立約束")
    
    componentPositioner2.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner2.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId7, None)
    
    theSession.DeleteUndoMark(markId8, None)
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner3 = workPart.ComponentAssembly.Positioner
    
    componentPositioner3.ClearNetwork()
    
    componentPositioner3.PrimaryArrangement = arrangement1
    
    componentPositioner3.BeginAssemblyConstraints()
    
    allowInterpartPositioning3 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression17 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression18 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression19 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression20 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression21 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression22 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression23 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression24 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network3 = componentPositioner3.EstablishNetwork()
    
    componentNetwork3 = network3
    componentNetwork3.MoveObjectsState = True
    
    componentNetwork3.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork3.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId10, "組立約束 對話方塊")
    
    componentNetwork3.MoveObjectsState = True
    
    componentNetwork3.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    component3 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 3 1")
    face5 = component3.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 140 {(20,0,-5.0000000000001) EXTRUDE(1)}")
    line4 = workPart.Lines.CreateFaceAxis(face5, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scaleAboutPoint53 = NXOpen.Point3d(-82.76218523018288, -83.065343417839287, 0.0)
    viewCenter53 = NXOpen.Point3d(82.762185230183078, 83.065343417839358, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint53, viewCenter53)
    
    scaleAboutPoint54 = NXOpen.Point3d(-106.10536567972164, -103.83167927229913, 0.0)
    viewCenter54 = NXOpen.Point3d(106.1053656797219, 103.8316792722992, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint54, viewCenter54)
    
    scaleAboutPoint55 = NXOpen.Point3d(-150.63172449174772, -157.73699451494352, 0.0)
    viewCenter55 = NXOpen.Point3d(150.63172449174795, 157.73699451494358, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint55, viewCenter55)
    
    scaleAboutPoint56 = NXOpen.Point3d(-120.50537959339815, -126.1895956119548, 0.0)
    viewCenter56 = NXOpen.Point3d(120.50537959339842, 126.18959561195487, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint56, viewCenter56)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = 0.38839409564435151
    rotMatrix5.Xy = 0.92107296714192444
    rotMatrix5.Xz = -0.027831918169188181
    rotMatrix5.Yx = -0.53724190742843614
    rotMatrix5.Yy = 0.25087408353954227
    rotMatrix5.Yz = 0.80525357938406428
    rotMatrix5.Zx = 0.74867961062877808
    rotMatrix5.Zy = -0.2978032629246441
    rotMatrix5.Zz = 0.59227701054504223
    translation5 = NXOpen.Point3d(49.624509253045254, -40.860506168625747, 19.682788709795041)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 0.87275667986661187)
    
    objects4 = [NXOpen.TaggedObject.Null] * 1 
    objects4[0] = line4
    nErrs10 = theSession.UpdateManager.AddObjectsToDeleteList(objects4)
    
    line5 = workPart.Lines.CreateFaceAxis(face5, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line5.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint57 = NXOpen.Point3d(-90.644298109247941, -72.151648662210789, 0.0)
    viewCenter57 = NXOpen.Point3d(90.64429810924814, 72.151648662210832, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint57, viewCenter57)
    
    scaleAboutPoint58 = NXOpen.Point3d(-73.000491587648483, -58.448898580143847, 0.0)
    viewCenter58 = NXOpen.Point3d(73.000491587648682, 58.448898580143883, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint58, viewCenter58)
    
    scaleAboutPoint59 = NXOpen.Point3d(-58.400393270118776, -46.759118864115088, 0.0)
    viewCenter59 = NXOpen.Point3d(58.400393270118926, 46.759118864115116, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint59, viewCenter59)
    
    objects5 = [NXOpen.TaggedObject.Null] * 1 
    objects5[0] = line5
    nErrs11 = theSession.UpdateManager.AddObjectsToDeleteList(objects5)
    
    scaleAboutPoint60 = NXOpen.Point3d(5.2773777307217751, -10.554755461443404, 0.0)
    viewCenter60 = NXOpen.Point3d(-5.2773777307216161, 10.554755461443444, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint60, viewCenter60)
    
    scaleAboutPoint61 = NXOpen.Point3d(7.3728071238024739, -11.447253165903691, 0.0)
    viewCenter61 = NXOpen.Point3d(-7.372807123802259, 11.447253165903724, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint61, viewCenter61)
    
    scaleAboutPoint62 = NXOpen.Point3d(10.428641655378435, -11.883800956128823, 0.0)
    viewCenter62 = NXOpen.Point3d(-10.42864165537827, 11.883800956128864, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint62, viewCenter62)
    
    scaleAboutPoint63 = NXOpen.Point3d(14.248434819848415, -13.035802069222939, 0.0)
    viewCenter63 = NXOpen.Point3d(-14.248434819848208, 13.035802069222964, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint63, viewCenter63)
    
    scaleAboutPoint64 = NXOpen.Point3d(39.410564395325295, -23.115811808796526, 0.0)
    viewCenter64 = NXOpen.Point3d(-39.410564395325039, 23.115811808796526, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint64, viewCenter64)
    
    scaleAboutPoint65 = NXOpen.Point3d(80.526393596217446, -25.105287415291329, 0.0)
    viewCenter65 = NXOpen.Point3d(-80.526393596217247, 25.105287415291329, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint65, viewCenter65)
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = 0.34342208612705177
    rotMatrix6.Xy = 0.18837372170851613
    rotMatrix6.Xz = 0.92009597962920231
    rotMatrix6.Yx = -0.5256214111542219
    rotMatrix6.Yy = 0.8504321462765706
    rotMatrix6.Yz = 0.022074798202177677
    rotMatrix6.Zx = -0.77832088684319856
    rotMatrix6.Zy = -0.49120312045945252
    rotMatrix6.Zz = 0.39107044321260725
    translation6 = NXOpen.Point3d(101.79051789144674, -4.9601183216063323, -85.540970561521448)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 0.44685142009170536)
    
    scaleAboutPoint66 = NXOpen.Point3d(150.39488215764132, 26.052656751717372, 0.0)
    viewCenter66 = NXOpen.Point3d(-150.39488215764112, -26.052656751717372, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint66, viewCenter66)
    
    scaleAboutPoint67 = NXOpen.Point3d(121.26327506253921, 22.736864074226084, 0.0)
    viewCenter67 = NXOpen.Point3d(-121.26327506253901, -22.736864074226084, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint67, viewCenter67)
    
    scaleAboutPoint68 = NXOpen.Point3d(97.389567784601851, 21.221073135944337, 0.0)
    viewCenter68 = NXOpen.Point3d(-97.389567784601539, -21.221073135944337, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint68, viewCenter68)
    
    scaleAboutPoint69 = NXOpen.Point3d(77.002179664712429, 18.795807634693528, 0.0)
    viewCenter69 = NXOpen.Point3d(-77.002179664712173, -18.795807634693556, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint69, viewCenter69)
    
    rotMatrix7 = NXOpen.Matrix3x3()
    
    rotMatrix7.Xx = -0.024872850719828844
    rotMatrix7.Xy = 0.077565049244109854
    rotMatrix7.Xz = 0.99667698098873891
    rotMatrix7.Yx = -0.051118267224889644
    rotMatrix7.Yy = 0.99558248443339825
    rotMatrix7.Yz = -0.078755567710134158
    rotMatrix7.Zx = -0.99838282439803183
    rotMatrix7.Zy = -0.052907275730087959
    rotMatrix7.Zz = -0.020797983600016324
    translation7 = NXOpen.Point3d(-15.719273654043601, 13.823231906676275, -84.743603420849226)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix7, translation7, 1.0909458498332649)
    
    scaleAboutPoint70 = NXOpen.Point3d(-2.4252655012506446, 59.176478230519102, 0.0)
    viewCenter70 = NXOpen.Point3d(2.4252655012509341, -59.176478230519102, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint70, viewCenter70)
    
    scaleAboutPoint71 = NXOpen.Point3d(-2.1342336411005509, 52.579756067116975, 0.0)
    viewCenter71 = NXOpen.Point3d(2.134233641100832, -52.579756067116975, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint71, viewCenter71)
    
    scaleAboutPoint72 = NXOpen.Point3d(-1.7073869128804011, 42.374238837853675, 0.0)
    viewCenter72 = NXOpen.Point3d(1.7073869128807186, -42.374238837853675, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint72, viewCenter72)
    
    scaleAboutPoint73 = NXOpen.Point3d(-1.365909530304289, 33.899391070282938, 0.0)
    viewCenter73 = NXOpen.Point3d(1.3659095303045961, -33.899391070282938, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint73, viewCenter73)
    
    scaleAboutPoint74 = NXOpen.Point3d(-1.0927276242434059, 27.119512856226343, 0.0)
    viewCenter74 = NXOpen.Point3d(1.0927276242437107, -27.119512856226351, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint74, viewCenter74)
    
    face6 = component1.FindObject("PROTO#.Features|EXTRUDE(4)|FACE 160 {(10,10,5) EXTRUDE(1)}")
    line6 = workPart.Lines.CreateFaceAxis(face6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line6.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint3 = componentPositioner3.CreateConstraint(True)
    
    componentConstraint3 = constraint3
    componentConstraint3.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.InferAlign
    
    componentConstraint3.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    face7 = component3.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 130 {(40,0,0) EXTRUDE(1)}")
    constraintReference5 = componentConstraint3.CreateConstraintReference(component3, face7, False, False, False)
    
    helpPoint5 = NXOpen.Point3d(-35.553692481201423, -139.09843298609513, 2.4053593941744111)
    constraintReference5.HelpPoint = helpPoint5
    
    face8 = component1.FindObject("PROTO#.Features|EXTRUDE(4)|FACE 130 {(20,10,10) EXTRUDE(1)}")
    constraintReference6 = componentConstraint3.CreateConstraintReference(component1, face8, False, False, False)
    
    helpPoint6 = NXOpen.Point3d(23.338913438308953, 47.46301807794854, 9.1552618980585958)
    constraintReference6.HelpPoint = helpPoint6
    
    constraintReference6.SetFixHint(True)
    
    componentConstraint3.SetAlignmentHint(NXOpen.Positioning.Constraint.Alignment.ContraAlign)
    
    objects6 = [NXOpen.TaggedObject.Null] * 1 
    objects6[0] = line6
    nErrs12 = theSession.UpdateManager.AddObjectsToDeleteList(objects6)
    
    componentNetwork3.Solve()
    
    scaleAboutPoint75 = NXOpen.Point3d(-3.0993728978542907, 16.688930988446977, 0.0)
    viewCenter75 = NXOpen.Point3d(3.0993728978545887, -16.688930988446984, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint75, viewCenter75)
    
    scaleAboutPoint76 = NXOpen.Point3d(-4.5695882468365161, 20.662485985696264, 0.0)
    viewCenter76 = NXOpen.Point3d(4.5695882468368287, -20.662485985696271, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint76, viewCenter76)
    
    scaleAboutPoint77 = NXOpen.Point3d(-6.4570268705299272, 25.82810748212033, 0.0)
    viewCenter77 = NXOpen.Point3d(6.4570268705302345, -25.82810748212033, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint77, viewCenter77)
    
    scaleAboutPoint78 = NXOpen.Point3d(-9.00258554064275, 32.129917360570367, 0.0)
    viewCenter78 = NXOpen.Point3d(9.0025855406430679, -32.129917360570367, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint78, viewCenter78)
    
    scaleAboutPoint79 = NXOpen.Point3d(-11.83529564610369, 37.834141819512219, 0.0)
    viewCenter79 = NXOpen.Point3d(11.835295646103955, -37.834141819512183, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint79, viewCenter79)
    
    scaleAboutPoint80 = NXOpen.Point3d(-15.764225758129971, 46.322571073889954, 0.0)
    viewCenter80 = NXOpen.Point3d(15.764225758130261, -46.322571073889897, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint80, viewCenter80)
    
    scaleAboutPoint81 = NXOpen.Point3d(-20.311598572975171, 56.993739279393388, 0.0)
    viewCenter81 = NXOpen.Point3d(20.311598572975431, -56.99373927939336, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint81, viewCenter81)
    
    rotMatrix8 = NXOpen.Matrix3x3()
    
    rotMatrix8.Xx = 0.71502617897974774
    rotMatrix8.Xy = 0.13327599247538302
    rotMatrix8.Xz = 0.68627623680506245
    rotMatrix8.Yx = -0.13953050137413925
    rotMatrix8.Yy = 0.98911537410758676
    rotMatrix8.Yz = -0.046712052944469076
    rotMatrix8.Zx = -0.68503197192532161
    rotMatrix8.Zy = -0.062356126673384166
    rotMatrix8.Zz = 0.72583945256949944
    translation8 = NXOpen.Point3d(22.34138382889379, 23.50213995461651, -71.483308106036645)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix8, translation8, 0.69820534389328981)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs13 = theSession.UpdateManager.DoUpdate(markId11)
    
    componentNetwork3.Solve()
    
    componentPositioner3.ClearNetwork()
    
    nErrs14 = theSession.UpdateManager.AddToDeleteList(componentNetwork3)
    
    componentPositioner3.DeleteNonPersistentConstraints()
    
    nErrs15 = theSession.UpdateManager.DoUpdate(markId11)
    
    theSession.DeleteUndoMark(markId13, None)
    
    theSession.SetUndoMarkName(markId10, "組立約束")
    
    componentPositioner3.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner3.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId11, None)
    
    theSession.DeleteUndoMark(markId12, None)
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner4 = workPart.ComponentAssembly.Positioner
    
    componentPositioner4.ClearNetwork()
    
    componentPositioner4.PrimaryArrangement = arrangement1
    
    componentPositioner4.BeginAssemblyConstraints()
    
    allowInterpartPositioning4 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression25 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression26 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression27 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression28 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression29 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression30 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression31 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression32 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network4 = componentPositioner4.EstablishNetwork()
    
    componentNetwork4 = network4
    componentNetwork4.MoveObjectsState = True
    
    componentNetwork4.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork4.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId14, "組立約束 對話方塊")
    
    componentNetwork4.MoveObjectsState = True
    
    componentNetwork4.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    scaleAboutPoint82 = NXOpen.Point3d(36.000034784191406, -120.50537959339822, 0.0)
    viewCenter82 = NXOpen.Point3d(-36.000034784191087, 120.50537959339827, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint82, viewCenter82)
    
    line7 = workPart.Lines.CreateFaceAxis(face5, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects7 = [NXOpen.TaggedObject.Null] * 1 
    objects7[0] = line7
    nErrs16 = theSession.UpdateManager.AddObjectsToDeleteList(objects7)
    
    scaleAboutPoint83 = NXOpen.Point3d(18.189491259381018, 32.437926079229236, 0.0)
    viewCenter83 = NXOpen.Point3d(-18.189491259380709, -32.437926079229157, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint83, viewCenter83)
    
    scaleAboutPoint84 = NXOpen.Point3d(22.357916339655826, 47.368466821304366, 0.0)
    viewCenter84 = NXOpen.Point3d(-22.357916339655375, -47.368466821304303, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint84, viewCenter84)
    
    scaleAboutPoint85 = NXOpen.Point3d(26.052656751717596, 69.631646227317361, 0.0)
    viewCenter85 = NXOpen.Point3d(-26.052656751717109, -69.631646227317319, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint85, viewCenter85)
    
    scaleAboutPoint86 = NXOpen.Point3d(41.447408468641456, 142.10540046391304, 0.0)
    viewCenter86 = NXOpen.Point3d(-41.447408468641051, -142.10540046391299, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint86, viewCenter86)
    
    scaleAboutPoint87 = NXOpen.Point3d(35.052665447765392, 114.63168970755648, 0.0)
    viewCenter87 = NXOpen.Point3d(-35.052665447764902, -114.63168970755643, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint87, viewCenter87)
    
    scaleAboutPoint88 = NXOpen.Point3d(29.557923296494121, 92.084299500615629, 0.0)
    viewCenter88 = NXOpen.Point3d(-29.557923296493701, -92.084299500615558, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint88, viewCenter88)
    
    scaleAboutPoint89 = NXOpen.Point3d(24.858971387820695, 73.667439600492514, 0.0)
    viewCenter89 = NXOpen.Point3d(-24.85897138782023, -73.667439600492443, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint89, viewCenter89)
    
    scaleAboutPoint90 = NXOpen.Point3d(20.129703660381704, 59.176478230519102, 0.0)
    viewCenter90 = NXOpen.Point3d(-20.129703660381249, -59.176478230519045, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint90, viewCenter90)
    
    scaleAboutPoint91 = NXOpen.Point3d(16.103762928305425, 47.341182584415293, 0.0)
    viewCenter91 = NXOpen.Point3d(-16.103762928304896, -47.341182584415215, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint91, viewCenter91)
    
    scaleAboutPoint92 = NXOpen.Point3d(12.883010342644381, 37.872946067532233, 0.0)
    viewCenter92 = NXOpen.Point3d(-12.883010342643878, -37.872946067532155, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint92, viewCenter92)
    
    scaleAboutPoint93 = NXOpen.Point3d(10.306408274115569, 30.298356854025791, 0.0)
    viewCenter93 = NXOpen.Point3d(-10.306408274115039, -30.298356854025727, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint93, viewCenter93)
    
    rotMatrix9 = NXOpen.Matrix3x3()
    
    rotMatrix9.Xx = 0.23392663802437347
    rotMatrix9.Xy = 0.098570846236517295
    rotMatrix9.Xz = 0.96724460003394663
    rotMatrix9.Yx = -0.013420462634493266
    rotMatrix9.Yy = 0.99507997273700921
    rotMatrix9.Yz = -0.098161800311468844
    rotMatrix9.Zx = -0.97216162195660039
    rotMatrix9.Zy = 0.0099817899161109332
    rotMatrix9.Zz = 0.23409857894652142
    translation9 = NXOpen.Point3d(-11.366462073447908, -33.25315926991351, -71.119032307078712)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix9, translation9, 2.6634420161944963)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint4 = componentPositioner4.CreateConstraint(True)
    
    componentConstraint4 = constraint4
    componentConstraint4.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge3 = component3.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 130 * 140 {(40,-2.5000000000001,4.3301270189223)(40,5.0000000000001,-0)(40,-2.5000000000001,-4.3301270189223) EXTRUDE(1)}")
    constraintReference7 = componentConstraint4.CreateConstraintReference(component3, edge3, False, False, False)
    
    helpPoint7 = NXOpen.Point3d(23.338913438327147, -144.97642417505216, 3.5375616229736986)
    constraintReference7.HelpPoint = helpPoint7
    
    edge4 = component1.FindObject("PROTO#.Features|EXTRUDE(4)|EDGE * 130 * 160 {(20,12.5,5.6698729810778)(20,5,10)(20,12.5,14.3301270189222) EXTRUDE(1)}")
    constraintReference8 = componentConstraint4.CreateConstraintReference(component1, edge4, False, False, False)
    
    helpPoint8 = NXOpen.Point3d(23.338913438327143, 46.280472943573059, 5.2223882867188678)
    constraintReference8.HelpPoint = helpPoint8
    
    constraintReference8.SetFixHint(True)
    
    componentNetwork4.Solve()
    
    scaleAboutPoint94 = NXOpen.Point3d(5.6623158710805113, 9.1391764936733821, 0.0)
    viewCenter94 = NXOpen.Point3d(-5.6623158710799348, -9.1391764936732969, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint94, viewCenter94)
    
    scaleAboutPoint95 = NXOpen.Point3d(7.0778948388505523, 11.175623429763638, 0.0)
    viewCenter95 = NXOpen.Point3d(-7.0778948388499803, -11.175623429763563, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint95, viewCenter95)
    
    scaleAboutPoint96 = NXOpen.Point3d(8.8473685485631375, 13.969529287204535, 0.0)
    viewCenter96 = NXOpen.Point3d(-8.8473685485625566, -13.969529287204468, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint96, viewCenter96)
    
    scaleAboutPoint97 = NXOpen.Point3d(11.447253165903939, 16.685826648605392, 0.0)
    viewCenter97 = NXOpen.Point3d(-11.447253165903394, -16.685826648605328, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint97, viewCenter97)
    
    rotMatrix10 = NXOpen.Matrix3x3()
    
    rotMatrix10.Xx = 0.96641267735125946
    rotMatrix10.Xy = 0.25395419240469752
    rotMatrix10.Xz = 0.039418336023224573
    rotMatrix10.Yx = -0.25215847524887108
    rotMatrix10.Yy = 0.90738664585856155
    rotMatrix10.Yz = 0.33625225393699293
    rotMatrix10.Zx = 0.049624997883390504
    rotMatrix10.Zy = -0.33489810850110974
    rotMatrix10.Zz = 0.9409466597567806
    translation10 = NXOpen.Point3d(59.23998024490222, -43.115889287036744, -18.775391256879981)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix10, translation10, 1.090945849833266)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs17 = theSession.UpdateManager.DoUpdate(markId15)
    
    componentNetwork4.Solve()
    
    componentPositioner4.ClearNetwork()
    
    nErrs18 = theSession.UpdateManager.AddToDeleteList(componentNetwork4)
    
    componentPositioner4.DeleteNonPersistentConstraints()
    
    nErrs19 = theSession.UpdateManager.DoUpdate(markId15)
    
    theSession.DeleteUndoMark(markId17, None)
    
    theSession.SetUndoMarkName(markId14, "組立約束")
    
    componentPositioner4.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner4.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId15, None)
    
    theSession.DeleteUndoMark(markId16, None)
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner5 = workPart.ComponentAssembly.Positioner
    
    componentPositioner5.ClearNetwork()
    
    componentPositioner5.PrimaryArrangement = arrangement1
    
    componentPositioner5.BeginAssemblyConstraints()
    
    allowInterpartPositioning5 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression33 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression34 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression35 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression36 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression37 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression38 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression39 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression40 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network5 = componentPositioner5.EstablishNetwork()
    
    componentNetwork5 = network5
    componentNetwork5.MoveObjectsState = True
    
    componentNetwork5.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork5.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId18, "組立約束 對話方塊")
    
    componentNetwork5.MoveObjectsState = True
    
    componentNetwork5.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    scaleAboutPoint98 = NXOpen.Point3d(-24.980234662882747, -46.565097624014967, 0.0)
    viewCenter98 = NXOpen.Point3d(24.980234662883326, 46.565097624014989, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint98, viewCenter98)
    
    scaleAboutPoint99 = NXOpen.Point3d(-19.984187730306147, -37.252078099211957, 0.0)
    viewCenter99 = NXOpen.Point3d(19.984187730306708, 37.252078099211985, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint99, viewCenter99)
    
    scaleAboutPoint100 = NXOpen.Point3d(-15.987350184244837, -29.801662479369561, 0.0)
    viewCenter100 = NXOpen.Point3d(15.987350184245432, 29.80166247936959, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint100, viewCenter100)
    
    scaleAboutPoint101 = NXOpen.Point3d(-19.984187730306115, -37.252078099211957, 0.0)
    viewCenter101 = NXOpen.Point3d(19.984187730306743, 37.252078099211985, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint101, viewCenter101)
    
    scaleAboutPoint102 = NXOpen.Point3d(-24.737708112757655, -45.109938323264487, 0.0)
    viewCenter102 = NXOpen.Point3d(24.737708112758234, 45.109938323264508, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint102, viewCenter102)
    
    scaleAboutPoint103 = NXOpen.Point3d(-30.922135140947162, -56.387422904080594, 0.0)
    viewCenter103 = NXOpen.Point3d(30.922135140947731, 56.387422904080623, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint103, viewCenter103)
    
    scaleAboutPoint104 = NXOpen.Point3d(16.673700321099314, -120.88432732796846, 0.0)
    viewCenter104 = NXOpen.Point3d(-16.673700321098735, 120.88432732796852, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint104, viewCenter104)
    
    scaleAboutPoint105 = NXOpen.Point3d(15.157909382817595, -142.10540046391282, 0.0)
    viewCenter105 = NXOpen.Point3d(-15.157909382817069, 142.10540046391287, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint105, viewCenter105)
    
    scaleAboutPoint106 = NXOpen.Point3d(21.315810069587222, -191.84229062628228, 0.0)
    viewCenter106 = NXOpen.Point3d(-21.315810069586618, 191.84229062628239, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint106, viewCenter106)
    
    scaleAboutPoint107 = NXOpen.Point3d(26.644762586983838, -242.02326016510139, 0.0)
    viewCenter107 = NXOpen.Point3d(-26.644762586983457, 242.02326016510165, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint107, viewCenter107)
    
    origin1 = NXOpen.Point3d(-2.2472465835668505, 27.40919792511048, 29.827619996801353)
    workPart.ModelingViews.WorkView.SetOrigin(origin1)
    
    origin2 = NXOpen.Point3d(-2.2472465835668505, 27.40919792511048, 29.827619996801353)
    workPart.ModelingViews.WorkView.SetOrigin(origin2)
    
    scaleAboutPoint108 = NXOpen.Point3d(-42.557606909765333, -246.09398778255724, 0.0)
    viewCenter108 = NXOpen.Point3d(42.557606909765809, 246.09398778255741, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint108, viewCenter108)
    
    scaleAboutPoint109 = NXOpen.Point3d(-31.825688645563563, -191.69426416746555, 0.0)
    viewCenter109 = NXOpen.Point3d(31.825688645564068, 191.6942641674658, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint109, viewCenter109)
    
    scaleAboutPoint110 = NXOpen.Point3d(-23.684233410651888, -149.80277632237454, 0.0)
    viewCenter110 = NXOpen.Point3d(23.684233410652343, 149.80277632237485, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint110, viewCenter110)
    
    scaleAboutPoint111 = NXOpen.Point3d(-16.578963387456273, -114.15800503934314, 0.0)
    viewCenter111 = NXOpen.Point3d(16.578963387456756, 114.15800503934338, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint111, viewCenter111)
    
    scaleAboutPoint112 = NXOpen.Point3d(-10.989484302542383, -84.12639707463623, 0.0)
    viewCenter112 = NXOpen.Point3d(10.989484302542802, 84.126397074636415, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint112, viewCenter112)
    
    scaleAboutPoint113 = NXOpen.Point3d(-10.610536567971961, -49.414784587984492, 0.0)
    viewCenter113 = NXOpen.Point3d(10.610536567972375, 49.414784587984727, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint113, viewCenter113)
    
    scaleAboutPoint114 = NXOpen.Point3d(-8.4884292543775288, -39.289301120262515, 0.0)
    viewCenter114 = NXOpen.Point3d(8.4884292543779427, 39.289301120262699, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint114, viewCenter114)
    
    component4 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 3 3")
    face9 = component4.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 140 {(20,0,-5.0000000000001) EXTRUDE(1)}")
    line8 = workPart.Lines.CreateFaceAxis(face9, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line8.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint115 = NXOpen.Point3d(-6.7907434035019909, -31.431440896209999, 0.0)
    viewCenter115 = NXOpen.Point3d(6.7907434035023879, 31.431440896210184, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint115, viewCenter115)
    
    scaleAboutPoint116 = NXOpen.Point3d(-5.4325947228015776, -24.058633772407628, 0.0)
    viewCenter116 = NXOpen.Point3d(5.4325947228019222, 24.058633772407813, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint116, viewCenter116)
    
    rotMatrix11 = NXOpen.Matrix3x3()
    
    rotMatrix11.Xx = 0.73556246145640836
    rotMatrix11.Xy = 0.5072114979248038
    rotMatrix11.Xz = -0.4490928207721257
    rotMatrix11.Yx = -0.014624429660656042
    rotMatrix11.Yy = 0.67464373736111749
    rotMatrix11.Yz = 0.73799861361422825
    rotMatrix11.Zx = 0.67729904130545437
    rotMatrix11.Zy = -0.53627635041301092
    rotMatrix11.Zz = 0.50366028693397047
    translation11 = NXOpen.Point3d(74.279254986538049, 105.73665494774211, -56.135490635019934)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix11, translation11, 2.1307536129555986)
    
    objects8 = [NXOpen.TaggedObject.Null] * 1 
    objects8[0] = line8
    nErrs20 = theSession.UpdateManager.AddObjectsToDeleteList(objects8)
    
    scaleAboutPoint117 = NXOpen.Point3d(-33.154349508298452, 5.5878117148818767, 0.0)
    viewCenter117 = NXOpen.Point3d(33.154349508298814, -5.5878117148817186, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint117, viewCenter117)
    
    scaleAboutPoint118 = NXOpen.Point3d(-41.442936885373094, 7.2951986277624261, 0.0)
    viewCenter118 = NXOpen.Point3d(41.442936885373491, -7.2951986277622538, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint118, viewCenter118)
    
    scaleAboutPoint119 = NXOpen.Point3d(-51.803671106716408, 9.5070407649031115, 0.0)
    viewCenter119 = NXOpen.Point3d(51.803671106716806, -9.5070407649029782, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint119, viewCenter119)
    
    scaleAboutPoint120 = NXOpen.Point3d(-55.781106528767729, 21.827389511257039, 0.0)
    viewCenter120 = NXOpen.Point3d(55.781106528768056, -21.827389511256953, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint120, viewCenter120)
    
    scaleAboutPoint121 = NXOpen.Point3d(-69.726383160959699, 27.284236889071291, 0.0)
    viewCenter121 = NXOpen.Point3d(69.726383160960054, -27.284236889071188, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint121, viewCenter121)
    
    scaleAboutPoint122 = NXOpen.Point3d(-86.021135747488373, 34.863191580479977, 0.0)
    viewCenter122 = NXOpen.Point3d(86.021135747488657, -34.86319158047985, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint122, viewCenter122)
    
    rotMatrix12 = NXOpen.Matrix3x3()
    
    rotMatrix12.Xx = 0.72957361975644253
    rotMatrix12.Xy = 0.57322959631014048
    rotMatrix12.Xz = -0.37300155933936119
    rotMatrix12.Yx = -0.68021933715008243
    rotMatrix12.Yy = 0.66474286282166717
    rotMatrix12.Yz = -0.30889897975674069
    rotMatrix12.Zx = 0.070880086925622129
    rotMatrix12.Zy = 0.47908742024996498
    rotMatrix12.Zz = 0.87490071267295733
    translation12 = NXOpen.Point3d(-9.6466464081867684, 97.990849115760554, -74.008875089554138)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix12, translation12, 0.55856427511463269)
    
    origin3 = NXOpen.Point3d(-3.7367145492395268, 85.277360284267544, 38.196817894004646)
    workPart.ModelingViews.WorkView.SetOrigin(origin3)
    
    origin4 = NXOpen.Point3d(-3.7367145492395268, 85.277360284267544, 38.196817894004646)
    workPart.ModelingViews.WorkView.SetOrigin(origin4)
    
    rotMatrix13 = NXOpen.Matrix3x3()
    
    rotMatrix13.Xx = 0.10825604822188219
    rotMatrix13.Xy = 0.97003568204008006
    rotMatrix13.Xz = 0.21751184701622572
    rotMatrix13.Yx = -0.11995296624725967
    rotMatrix13.Yy = 0.22994499857039402
    rotMatrix13.Yz = -0.96578288632639253
    rotMatrix13.Zx = -0.98685962219145251
    rotMatrix13.Zy = 0.078460647470500522
    rotMatrix13.Zz = 0.14125159428000725
    translation13 = NXOpen.Point3d(-69.07218901614894, -14.679241499839232, -147.89400908809733)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix13, translation13, 0.55856427511463269)
    
    scaleAboutPoint123 = NXOpen.Point3d(64.42111487697386, 0.47368466821305583, 0.0)
    viewCenter123 = NXOpen.Point3d(-64.421114876973661, -0.47368466821297506, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint123, viewCenter123)
    
    scaleAboutPoint124 = NXOpen.Point3d(51.915839636149528, 0.37894773457047698, 0.0)
    viewCenter124 = NXOpen.Point3d(-51.915839636149272, -0.37894773457034769, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint124, viewCenter124)
    
    scaleAboutPoint125 = NXOpen.Point3d(42.138988084232359, 1.2126327506254486, 0.0)
    viewCenter125 = NXOpen.Point3d(-42.138988084232125, -1.2126327506252936, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint125, viewCenter125)
    
    scaleAboutPoint126 = NXOpen.Point3d(33.953717017510947, 1.9402124010006971, 0.0)
    viewCenter126 = NXOpen.Point3d(-33.953717017510762, -1.9402124010005524, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint126, viewCenter126)
    
    scaleAboutPoint127 = NXOpen.Point3d(27.356994854108837, 3.8804248020013024, 0.0)
    viewCenter127 = NXOpen.Point3d(-27.35699485410867, -3.88042480200117, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint127, viewCenter127)
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint5 = componentPositioner5.CreateConstraint(True)
    
    componentConstraint5 = constraint5
    componentConstraint5.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.InferAlign
    
    componentConstraint5.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    component5 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT 3 4")
    face10 = component5.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 130 {(40,0,0) EXTRUDE(1)}")
    constraintReference9 = componentConstraint5.CreateConstraintReference(component5, face10, False, False, False)
    
    helpPoint9 = NXOpen.Point3d(-12.2191687020453, -184.52384273515861, 2.787828566169992)
    constraintReference9.HelpPoint = helpPoint9
    
    face11 = component1.FindObject("PROTO#.Features|EXTRUDE(4)|FACE 150 {(20,90,6) EXTRUDE(1)}")
    constraintReference10 = componentConstraint5.CreateConstraintReference(component1, face11, False, False, False)
    
    helpPoint10 = NXOpen.Point3d(23.338913438308953, 123.07598381289611, 4.1078956568014737)
    constraintReference10.HelpPoint = helpPoint10
    
    constraintReference10.SetFixHint(True)
    
    componentConstraint5.SetAlignmentHint(NXOpen.Positioning.Constraint.Alignment.ContraAlign)
    
    componentNetwork5.Solve()
    
    scaleAboutPoint128 = NXOpen.Point3d(-78.695014984585114, 11.330840421843678, 0.0)
    viewCenter128 = NXOpen.Point3d(78.695014984585271, -11.330840421843545, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint128, viewCenter128)
    
    scaleAboutPoint129 = NXOpen.Point3d(-98.756811210931531, 13.77550804710447, 0.0)
    viewCenter129 = NXOpen.Point3d(98.756811210931701, -13.775508047104337, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint129, viewCenter129)
    
    scaleAboutPoint130 = NXOpen.Point3d(-123.6885405637895, 16.734331958630438, 0.0)
    viewCenter130 = NXOpen.Point3d(123.68854056378967, -16.734331958630293, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint130, viewCenter130)
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs21 = theSession.UpdateManager.DoUpdate(markId19)
    
    componentNetwork5.Solve()
    
    componentPositioner5.ClearNetwork()
    
    nErrs22 = theSession.UpdateManager.AddToDeleteList(componentNetwork5)
    
    componentPositioner5.DeleteNonPersistentConstraints()
    
    nErrs23 = theSession.UpdateManager.DoUpdate(markId19)
    
    theSession.DeleteUndoMark(markId21, None)
    
    theSession.SetUndoMarkName(markId18, "組立約束")
    
    componentPositioner5.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner5.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId19, None)
    
    theSession.DeleteUndoMark(markId20, None)
    
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner6 = workPart.ComponentAssembly.Positioner
    
    componentPositioner6.ClearNetwork()
    
    componentPositioner6.PrimaryArrangement = arrangement1
    
    componentPositioner6.BeginAssemblyConstraints()
    
    allowInterpartPositioning6 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression41 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression42 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression43 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression44 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression45 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression46 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression47 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression48 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network6 = componentPositioner6.EstablishNetwork()
    
    componentNetwork6 = network6
    componentNetwork6.MoveObjectsState = True
    
    componentNetwork6.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork6.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId22, "組立約束 對話方塊")
    
    componentNetwork6.MoveObjectsState = True
    
    componentNetwork6.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    scaleAboutPoint131 = NXOpen.Point3d(-171.89069240114867, -42.745304459544855, 0.0)
    viewCenter131 = NXOpen.Point3d(171.89069240114884, 42.745304459545011, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint131, viewCenter131)
    
    scaleAboutPoint132 = NXOpen.Point3d(-265.64236193387399, -6.8210592222677429, 0.0)
    viewCenter132 = NXOpen.Point3d(265.6423619338741, 6.8210592222679045, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint132, viewCenter132)
    
    scaleAboutPoint133 = NXOpen.Point3d(-331.1055830809164, -9.4736933642607895, 0.0)
    viewCenter133 = NXOpen.Point3d(331.10558308091652, 9.4736933642609511, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint133, viewCenter133)
    
    scaleAboutPoint134 = NXOpen.Point3d(-413.8819788511455, -12.434222540592256, 0.0)
    viewCenter134 = NXOpen.Point3d(413.88197885114562, 12.434222540592456, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint134, viewCenter134)
    
    origin5 = NXOpen.Point3d(-130.1811974857427, 198.27033618899716, 27.376843348305066)
    workPart.ModelingViews.WorkView.SetOrigin(origin5)
    
    origin6 = NXOpen.Point3d(-130.1811974857427, 198.27033618899716, 27.376843348305066)
    workPart.ModelingViews.WorkView.SetOrigin(origin6)
    
    scaleAboutPoint135 = NXOpen.Point3d(-345.64178133670424, -97.697462818939812, 0.0)
    viewCenter135 = NXOpen.Point3d(345.64178133670424, 97.697462818940068, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint135, viewCenter135)
    
    scaleAboutPoint136 = NXOpen.Point3d(-288.35554177468936, -77.565864419885557, 0.0)
    viewCenter136 = NXOpen.Point3d(288.35554177468947, 77.565864419885813, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint136, viewCenter136)
    
    scaleAboutPoint137 = NXOpen.Point3d(-234.94759543366888, -61.105322199482309, 0.0)
    viewCenter137 = NXOpen.Point3d(234.94759543366888, 61.105322199482586, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint137, viewCenter137)
    
    scaleAboutPoint138 = NXOpen.Point3d(-189.47386728521684, -48.884257759585815, 0.0)
    viewCenter138 = NXOpen.Point3d(189.47386728521684, 48.884257759586106, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint138, viewCenter138)
    
    scaleAboutPoint139 = NXOpen.Point3d(-151.88225201582981, -39.107406207668596, 0.0)
    viewCenter139 = NXOpen.Point3d(151.88225201582981, 39.107406207668909, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint139, viewCenter139)
    
    scaleAboutPoint140 = NXOpen.Point3d(58.20637203001862, 22.312442611507297, 0.0)
    viewCenter140 = NXOpen.Point3d(-58.206372030018642, -22.312442611506984, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint140, viewCenter140)
    
    scaleAboutPoint141 = NXOpen.Point3d(72.757965037523277, 27.890553264384067, 0.0)
    viewCenter141 = NXOpen.Point3d(-72.757965037523277, -27.890553264383758, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint141, viewCenter141)
    
    scaleAboutPoint142 = NXOpen.Point3d(90.947456296904036, 34.863191580480056, 0.0)
    viewCenter142 = NXOpen.Point3d(-90.947456296904164, -34.863191580479729, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint142, viewCenter142)
    
    scaleAboutPoint143 = NXOpen.Point3d(113.68432037113004, 44.052674143813121, 0.0)
    viewCenter143 = NXOpen.Point3d(-113.6843203711302, -44.052674143812716, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint143, viewCenter143)
    
    line9 = workPart.Lines.CreateFaceAxis(face5, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scaleAboutPoint144 = NXOpen.Point3d(283.02658925729253, 79.934287760951065, 0.0)
    viewCenter144 = NXOpen.Point3d(-283.02658925729276, -79.934287760950653, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint144, viewCenter144)
    
    scaleAboutPoint145 = NXOpen.Point3d(227.84232541047328, 63.947430208760899, 0.0)
    viewCenter145 = NXOpen.Point3d(-227.84232541047336, -63.947430208760501, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint145, viewCenter145)
    
    scaleAboutPoint146 = NXOpen.Point3d(183.41070353208985, 51.15794416700875, 0.0)
    viewCenter146 = NXOpen.Point3d(-183.41070353208997, -51.15794416700836, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint146, viewCenter146)
    
    scaleAboutPoint147 = NXOpen.Point3d(147.03172101332811, 40.926355333607042, 0.0)
    viewCenter147 = NXOpen.Point3d(-147.03172101332822, -40.926355333606622, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint147, viewCenter147)
    
    scaleAboutPoint148 = NXOpen.Point3d(117.86790336078762, 32.7410842668857, 0.0)
    viewCenter148 = NXOpen.Point3d(-117.86790336078775, -32.741084266885267, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint148, viewCenter148)
    
    scaleAboutPoint149 = NXOpen.Point3d(77.414474799924761, 34.341759497711209, 0.0)
    viewCenter149 = NXOpen.Point3d(-77.414474799924818, -34.341759497710783, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint149, viewCenter149)
    
    scaleAboutPoint150 = NXOpen.Point3d(60.689843903299398, 27.473407598169011, 0.0)
    viewCenter150 = NXOpen.Point3d(-60.689843903299476, -27.473407598168585, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint150, viewCenter150)
    
    scaleAboutPoint151 = NXOpen.Point3d(48.179354341647375, 21.97872607853526, 0.0)
    viewCenter151 = NXOpen.Point3d(-48.179354341647482, -21.978726078534816, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint151, viewCenter151)
    
    scaleAboutPoint152 = NXOpen.Point3d(38.543483473317885, 17.582980862828258, 0.0)
    viewCenter152 = NXOpen.Point3d(-38.54348347331802, -17.582980862827799, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint152, viewCenter152)
    
    face12 = component1.FindObject("PROTO#.Features|EXTRUDE(4)|FACE 170 {(10,90,1) EXTRUDE(1)}")
    line10 = workPart.Lines.CreateFaceAxis(face12, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint6 = componentPositioner6.CreateConstraint(True)
    
    componentConstraint6 = constraint6
    componentConstraint6.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge5 = component4.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 130 * 140 {(40,-2.5000000000001,4.3301270189223)(40,5.0000000000001,-0)(40,-2.5000000000001,-4.3301270189223) EXTRUDE(1)}")
    constraintReference11 = componentConstraint6.CreateConstraintReference(component4, edge5, False, False, False)
    
    helpPoint11 = NXOpen.Point3d(34.44987885630335, -181.96964911738706, 4.998786567874772)
    constraintReference11.HelpPoint = helpPoint11
    
    edge6 = component1.FindObject("PROTO#.Features|EXTRUDE(4)|EDGE * 150 * 170 {(20,92.5,1.6698729810778)(20,85,6)(20,92.5,10.3301270189222) EXTRUDE(1)}")
    constraintReference12 = componentConstraint6.CreateConstraintReference(component1, edge6, False, False, False)
    
    helpPoint12 = NXOpen.Point3d(23.338913438327143, 123.08269910453303, 1.3063180869250002)
    constraintReference12.HelpPoint = helpPoint12
    
    constraintReference12.SetFixHint(True)
    
    objects9 = [NXOpen.TaggedObject.Null] * 1 
    objects9[0] = line10
    nErrs24 = theSession.UpdateManager.AddObjectsToDeleteList(objects9)
    
    objects10 = [NXOpen.TaggedObject.Null] * 1 
    objects10[0] = line9
    nErrs25 = theSession.UpdateManager.AddObjectsToDeleteList(objects10)
    
    componentNetwork6.Solve()
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs26 = theSession.UpdateManager.DoUpdate(markId23)
    
    componentNetwork6.Solve()
    
    componentPositioner6.ClearNetwork()
    
    nErrs27 = theSession.UpdateManager.AddToDeleteList(componentNetwork6)
    
    componentPositioner6.DeleteNonPersistentConstraints()
    
    nErrs28 = theSession.UpdateManager.DoUpdate(markId23)
    
    theSession.DeleteUndoMark(markId25, None)
    
    theSession.SetUndoMarkName(markId22, "組立約束")
    
    componentPositioner6.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner6.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId23, None)
    
    theSession.DeleteUndoMark(markId24, None)
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner7 = workPart.ComponentAssembly.Positioner
    
    componentPositioner7.ClearNetwork()
    
    componentPositioner7.PrimaryArrangement = arrangement1
    
    componentPositioner7.BeginAssemblyConstraints()
    
    allowInterpartPositioning7 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression49 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression50 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression51 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression52 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression53 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression54 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression55 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression56 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network7 = componentPositioner7.EstablishNetwork()
    
    componentNetwork7 = network7
    componentNetwork7.MoveObjectsState = True
    
    componentNetwork7.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork7.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId26, "組立約束 對話方塊")
    
    componentNetwork7.MoveObjectsState = True
    
    componentNetwork7.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    scaleAboutPoint153 = NXOpen.Point3d(-29.8811335793146, -5.8013902959837074, 0.0)
    viewCenter153 = NXOpen.Point3d(29.881133579314437, 5.8013902959841612, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint153, viewCenter153)
    
    scaleAboutPoint154 = NXOpen.Point3d(-37.848111348799399, -6.9537212451859975, 0.0)
    viewCenter154 = NXOpen.Point3d(37.848111348799215, 6.953721245186455, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint154, viewCenter154)
    
    scaleAboutPoint155 = NXOpen.Point3d(-47.434312779663259, -8.6921515564825622, 0.0)
    viewCenter155 = NXOpen.Point3d(47.434312779663095, 8.692151556483017, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint155, viewCenter155)
    
    scaleAboutPoint156 = NXOpen.Point3d(-59.292890974579038, -10.865189445603271, 0.0)
    viewCenter156 = NXOpen.Point3d(59.292890974578903, 10.86518944560372, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint156, viewCenter156)
    
    scaleAboutPoint157 = NXOpen.Point3d(-74.116113718223772, -13.581486807004117, 0.0)
    viewCenter157 = NXOpen.Point3d(74.11611371822363, 13.58148680700458, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint157, viewCenter157)
    
    rotMatrix14 = NXOpen.Matrix3x3()
    
    rotMatrix14.Xx = -0.60192589089967052
    rotMatrix14.Xy = -0.79765868491218728
    rotMatrix14.Xz = 0.037760352868997919
    rotMatrix14.Yx = -0.051574803987507148
    rotMatrix14.Yy = -0.0083551641987914052
    rotMatrix14.Yz = -0.99863418268395931
    rotMatrix14.Zx = 0.79688472281646927
    rotMatrix14.Zy = -0.60305125289262373
    rotMatrix14.Zz = -0.036109900669307832
    translation14 = NXOpen.Point3d(-20.948631808165111, -15.074877319836261, -224.93422023405262)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix14, translation14, 1.0909458498332674)
    
    rotMatrix15 = NXOpen.Matrix3x3()
    
    rotMatrix15.Xx = 0.22565720881539253
    rotMatrix15.Xy = -0.9741876642854046
    rotMatrix15.Xz = -0.0061007264971995141
    rotMatrix15.Yx = -0.062993793833935399
    rotMatrix15.Yy = -0.0083419311524776316
    rotMatrix15.Yz = -0.99797905495208428
    rotMatrix15.Zx = 0.97216799270910659
    rotMatrix15.Zy = 0.22558547590391234
    rotMatrix15.Zz = -0.06325019377955611
    translation15 = NXOpen.Point3d(30.285683923918192, -15.845357923245484, -191.36432560491909)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix15, translation15, 1.0909458498332674)
    
    scaleAboutPoint158 = NXOpen.Point3d(-89.249770446028634, -30.800871865884627, 0.0)
    viewCenter158 = NXOpen.Point3d(89.249770446028464, 30.800871865885082, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint158, viewCenter158)
    
    scaleAboutPoint159 = NXOpen.Point3d(-69.653625195922388, -26.192867413508161, 0.0)
    viewCenter159 = NXOpen.Point3d(69.653625195922189, 26.192867413508608, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint159, viewCenter159)
    
    scaleAboutPoint160 = NXOpen.Point3d(-53.394645275537179, -22.196029867446878, 0.0)
    viewCenter160 = NXOpen.Point3d(53.394645275536973, 22.19602986744734, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint160, viewCenter160)
    
    scaleAboutPoint161 = NXOpen.Point3d(-41.349806690125327, -18.253518268613604, 0.0)
    viewCenter161 = NXOpen.Point3d(41.349806690125106, 18.253518268614059, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint161, viewCenter161)
    
    scaleAboutPoint162 = NXOpen.Point3d(-31.788439977994287, -14.602814614890832, 0.0)
    viewCenter162 = NXOpen.Point3d(31.788439977994052, 14.602814614891297, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint162, viewCenter162)
    
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint7 = componentPositioner7.CreateConstraint(True)
    
    componentConstraint7 = constraint7
    componentConstraint7.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.InferAlign
    
    componentConstraint7.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    constraintReference13 = componentConstraint7.CreateConstraintReference(component5, face10, False, False, False)
    
    helpPoint13 = NXOpen.Point3d(23.338913438290767, -182.31804686271687, -2.1468315609709521)
    constraintReference13.HelpPoint = helpPoint13
    
    face13 = component1.FindObject("PROTO#.Features|EXTRUDE(3)|FACE 130 {(30,90,6) EXTRUDE(1)}")
    constraintReference14 = componentConstraint7.CreateConstraintReference(component1, face13, False, False, False)
    
    helpPoint14 = NXOpen.Point3d(33.338913438299862, 122.24637109761719, 7.1936266532901518)
    constraintReference14.HelpPoint = helpPoint14
    
    constraintReference14.SetFixHint(True)
    
    componentConstraint7.SetAlignmentHint(NXOpen.Positioning.Constraint.Alignment.ContraAlign)
    
    componentNetwork7.Solve()
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs29 = theSession.UpdateManager.DoUpdate(markId27)
    
    componentNetwork7.Solve()
    
    componentPositioner7.ClearNetwork()
    
    nErrs30 = theSession.UpdateManager.AddToDeleteList(componentNetwork7)
    
    componentPositioner7.DeleteNonPersistentConstraints()
    
    nErrs31 = theSession.UpdateManager.DoUpdate(markId27)
    
    theSession.DeleteUndoMark(markId29, None)
    
    theSession.SetUndoMarkName(markId26, "組立約束")
    
    componentPositioner7.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner7.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId27, None)
    
    theSession.DeleteUndoMark(markId28, None)
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner8 = workPart.ComponentAssembly.Positioner
    
    componentPositioner8.ClearNetwork()
    
    componentPositioner8.PrimaryArrangement = arrangement1
    
    componentPositioner8.BeginAssemblyConstraints()
    
    allowInterpartPositioning8 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression57 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression58 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression59 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression60 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression61 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression62 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression63 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression64 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network8 = componentPositioner8.EstablishNetwork()
    
    componentNetwork8 = network8
    componentNetwork8.MoveObjectsState = True
    
    componentNetwork8.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork8.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId30, "組立約束 對話方塊")
    
    componentNetwork8.MoveObjectsState = True
    
    componentNetwork8.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    scaleAboutPoint163 = NXOpen.Point3d(-3.3377861976895091, -6.8345145952685185, 0.0)
    viewCenter163 = NXOpen.Point3d(3.3377861976892649, 6.8345145952689732, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint163, viewCenter163)
    
    scaleAboutPoint164 = NXOpen.Point3d(-1.4900831239686116, -7.6490933697046213, 0.0)
    viewCenter164 = NXOpen.Point3d(1.4900831239683405, 7.6490933697050787, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint164, viewCenter164)
    
    scaleAboutPoint165 = NXOpen.Point3d(-1.8626039049607011, -9.5613667121308303, 0.0)
    viewCenter165 = NXOpen.Point3d(1.8626039049604681, 9.5613667121312851, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint165, viewCenter165)
    
    scaleAboutPoint166 = NXOpen.Point3d(-2.3282548812008499, -11.95170839016359, 0.0)
    viewCenter166 = NXOpen.Point3d(2.3282548812006119, 11.951708390164066, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint166, viewCenter166)
    
    scaleAboutPoint167 = NXOpen.Point3d(-2.9103186015010296, -14.939635487704555, 0.0)
    viewCenter167 = NXOpen.Point3d(2.9103186015008142, 14.939635487705019, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint167, viewCenter167)
    
    scaleAboutPoint168 = NXOpen.Point3d(42.199619721763312, -22.797495711757062, 0.0)
    viewCenter168 = NXOpen.Point3d(-42.199619721763604, 22.797495711757517, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint168, viewCenter168)
    
    scaleAboutPoint169 = NXOpen.Point3d(52.749524652204201, -28.496869639696381, 0.0)
    viewCenter169 = NXOpen.Point3d(-52.749524652204514, 28.496869639696847, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint169, viewCenter169)
    
    rotMatrix16 = NXOpen.Matrix3x3()
    
    rotMatrix16.Xx = -0.42900565650755701
    rotMatrix16.Xy = -0.89803744294660326
    rotMatrix16.Xz = 0.097380171238532182
    rotMatrix16.Yx = -0.25308400283198956
    rotMatrix16.Yy = 0.01600988636411425
    rotMatrix16.Yz = -0.96731182720420894
    rotMatrix16.Zx = 0.86712319435882723
    rotMatrix16.Zy = -0.43962760901077852
    rotMatrix16.Zz = -0.23414724256417893
    translation16 = NXOpen.Point3d(65.258475689320036, -31.389430804259803, -213.99938512799085)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix16, translation16, 0.69820534389329147)
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Suppress Constraint")
    
    componentConstraint7.Suppressed = True
    
    componentNetwork8.Solve()
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide Component")
    
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide Component")
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Show Component")
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Show Component")
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete Constraint")
    
    objects11 = [NXOpen.TaggedObject.Null] * 1 
    objects11[0] = componentConstraint7
    nErrs32 = theSession.UpdateManager.AddObjectsToDeleteList(objects11)
    
    componentNetwork8.Solve()
    
    # ----------------------------------------------
    #   功能表：組立件(A)->元件位置(P)->組立約束(N)...
    # ----------------------------------------------
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    theSession.DeleteUndoMark(markId38, None)
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs33 = theSession.UpdateManager.DoUpdate(markId31)
    
    componentNetwork8.Solve()
    
    componentPositioner8.ClearNetwork()
    
    nErrs34 = theSession.UpdateManager.AddToDeleteList(componentNetwork8)
    
    componentPositioner8.DeleteNonPersistentConstraints()
    
    nErrs35 = theSession.UpdateManager.DoUpdate(markId31)
    
    theSession.DeleteUndoMark(markId39, None)
    
    theSession.SetUndoMarkName(markId30, "組立約束")
    
    componentPositioner8.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner8.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId31, None)
    
    theSession.DeleteUndoMark(markId37, None)
    
    theSession.DeleteUndoMark(markId32, None)
    
    theSession.DeleteUndoMark(markId1, None)
    
    markId40 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "通過定位任務建立約束")
    
    markId41 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    componentPositioner9 = workPart.ComponentAssembly.Positioner
    
    componentPositioner9.ClearNetwork()
    
    componentPositioner9.PrimaryArrangement = arrangement1
    
    componentPositioner9.BeginAssemblyConstraints()
    
    allowInterpartPositioning9 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression65 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression66 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression67 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression68 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression69 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression70 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression71 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression72 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network9 = componentPositioner9.EstablishNetwork()
    
    componentNetwork9 = network9
    componentNetwork9.MoveObjectsState = True
    
    componentNetwork9.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork9.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId41, "組立約束 對話方塊")
    
    componentNetwork9.MoveObjectsState = True
    
    componentNetwork9.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId42 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    scaleAboutPoint170 = NXOpen.Point3d(206.90546307545654, -39.41056439532489, 0.0)
    viewCenter170 = NXOpen.Point3d(-206.90546307545694, 39.410564395325338, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint170, viewCenter170)
    
    scaleAboutPoint171 = NXOpen.Point3d(167.04016139864694, -32.134767891572544, 0.0)
    viewCenter171 = NXOpen.Point3d(-167.04016139864726, 32.134767891573013, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint171, viewCenter171)
    
    scaleAboutPoint172 = NXOpen.Point3d(136.29992117029337, -26.677920513758291, 0.0)
    viewCenter172 = NXOpen.Point3d(-136.29992117029371, 26.677920513758789, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint172, viewCenter172)
    
    scaleAboutPoint173 = NXOpen.Point3d(117.38285026053728, -22.50646385160697, 0.0)
    viewCenter173 = NXOpen.Point3d(-117.38285026053768, 22.506463851607432, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint173, viewCenter173)
    
    face14 = component5.FindObject("PROTO#.Features|EXTRUDE(1)|FACE 140 {(20,0,-5.0000000000001) EXTRUDE(1)}")
    line11 = workPart.Lines.CreateFaceAxis(face14, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line11.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects12 = [NXOpen.TaggedObject.Null] * 1 
    objects12[0] = line11
    nErrs36 = theSession.UpdateManager.AddObjectsToDeleteList(objects12)
    
    scaleAboutPoint174 = NXOpen.Point3d(-13.814312295124584, -2.9491228495207222, 0.0)
    viewCenter174 = NXOpen.Point3d(13.814312295124253, 2.9491228495211721, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint174, viewCenter174)
    
    scaleAboutPoint175 = NXOpen.Point3d(-43.266736542313993, -3.880424802001019, 0.0)
    viewCenter175 = NXOpen.Point3d(43.266736542313645, 3.8804248020014822, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint175, viewCenter175)
    
    scaleAboutPoint176 = NXOpen.Point3d(-78.093549140275115, -6.063163753126716, 0.0)
    viewCenter176 = NXOpen.Point3d(78.093549140274789, 6.0631637531271716, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint176, viewCenter176)
    
    scaleAboutPoint177 = NXOpen.Point3d(-123.99169875144604, -10.307378380315569, 0.0)
    viewCenter177 = NXOpen.Point3d(123.9916987514457, 10.30737838031601, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint177, viewCenter177)
    
    rotMatrix17 = NXOpen.Matrix3x3()
    
    rotMatrix17.Xx = 0.011034327127961667
    rotMatrix17.Xy = -0.99987610841011176
    rotMatrix17.Xz = -0.011225482416432645
    rotMatrix17.Yx = -0.16413797817202688
    rotMatrix17.Yy = 0.0092627428094221049
    rotMatrix17.Yz = -0.98639389987836246
    rotMatrix17.Zx = 0.98637567272638516
    rotMatrix17.Zy = 0.012726720956122832
    rotMatrix17.Zz = -0.16401543472268845
    translation17 = NXOpen.Point3d(-97.171351769970641, -7.0751325487961001, -194.94578667204161)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix17, translation17, 0.69820534389329159)
    
    scaleAboutPoint178 = NXOpen.Point3d(-230.02127488425327, -24.631602747077974, 0.0)
    viewCenter178 = NXOpen.Point3d(230.02127488425302, 24.631602747078425, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint178, viewCenter178)
    
    scaleAboutPoint179 = NXOpen.Point3d(-183.41070353209003, -19.705282197662306, 0.0)
    viewCenter179 = NXOpen.Point3d(183.41070353208971, 19.705282197662797, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint179, viewCenter179)
    
    scaleAboutPoint180 = NXOpen.Point3d(-146.48603627554698, -15.764225758129825, 0.0)
    viewCenter180 = NXOpen.Point3d(146.4860362755467, 15.7642257581303, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint180, viewCenter180)
    
    scaleAboutPoint181 = NXOpen.Point3d(-116.41274406003733, -12.223338126303673, 0.0)
    viewCenter181 = NXOpen.Point3d(116.41274406003706, 12.223338126304153, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint181, viewCenter181)
    
    scaleAboutPoint182 = NXOpen.Point3d(-91.733242319309454, -9.0025855406426416, 0.0)
    viewCenter182 = NXOpen.Point3d(91.733242319309142, 9.0025855406431177, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint182, viewCenter182)
    
    face15 = component1.FindObject("PROTO#.Features|EXTRUDE(3)|FACE 160 {(40,90,11) EXTRUDE(1)}")
    line12 = workPart.Lines.CreateFaceAxis(face15, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line12.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint183 = NXOpen.Point3d(-72.020684325143193, -6.5812004641938771, 0.0)
    viewCenter183 = NXOpen.Point3d(72.020684325142838, 6.5812004641943433, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint183, viewCenter183)
    
    scaleAboutPoint184 = NXOpen.Point3d(-57.616547460114575, -5.2649603713550501, 0.0)
    viewCenter184 = NXOpen.Point3d(57.616547460114248, 5.2649603713555244, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint184, viewCenter184)
    
    scaleAboutPoint185 = NXOpen.Point3d(-46.093237968091699, -4.2119682970839927, 0.0)
    viewCenter185 = NXOpen.Point3d(46.093237968091351, 4.211968297084467, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint185, viewCenter185)
    
    scaleAboutPoint186 = NXOpen.Point3d(-36.874590374473406, -3.3695746376671467, 0.0)
    viewCenter186 = NXOpen.Point3d(36.874590374473051, 3.3695746376676237, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint186, viewCenter186)
    
    scaleAboutPoint187 = NXOpen.Point3d(-29.44881079561398, -2.5939367022040862, 0.0)
    viewCenter187 = NXOpen.Point3d(29.448810795613632, 2.5939367022045636, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint187, viewCenter187)
    
    markId43 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint8 = componentPositioner9.CreateConstraint(True)
    
    componentConstraint8 = constraint8
    componentConstraint8.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.InferAlign
    
    componentConstraint8.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    constraintReference15 = componentConstraint8.CreateConstraintReference(component5, face10, False, False, False)
    
    helpPoint15 = NXOpen.Point3d(23.338913438290767, -181.4884882666928, -1.996312717778892)
    constraintReference15.HelpPoint = helpPoint15
    
    constraintReference16 = componentConstraint8.CreateConstraintReference(component1, face13, False, False, False)
    
    helpPoint16 = NXOpen.Point3d(33.338913438299862, 127.52574759223026, 7.9469747955158692)
    constraintReference16.HelpPoint = helpPoint16
    
    constraintReference16.SetFixHint(True)
    
    componentConstraint8.SetAlignmentHint(NXOpen.Positioning.Constraint.Alignment.ContraAlign)
    
    objects13 = [NXOpen.TaggedObject.Null] * 1 
    objects13[0] = line12
    nErrs37 = theSession.UpdateManager.AddObjectsToDeleteList(objects13)
    
    componentNetwork9.Solve()
    
    scaleAboutPoint188 = NXOpen.Point3d(-15.828100033843038, 0.85447326660871947, 0.0)
    viewCenter188 = NXOpen.Point3d(15.828100033842698, -0.85447326660824419, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint188, viewCenter188)
    
    scaleAboutPoint189 = NXOpen.Point3d(-18.615310451113565, 0.9155070713664708, 0.0)
    viewCenter189 = NXOpen.Point3d(18.615310451113217, -0.91550707136599385, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint189, viewCenter189)
    
    scaleAboutPoint190 = NXOpen.Point3d(-22.760523024243991, 1.0808069592520384, 0.0)
    viewCenter190 = NXOpen.Point3d(22.760523024243664, -1.0808069592515559, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint190, viewCenter190)
    
    scaleAboutPoint191 = NXOpen.Point3d(-28.371182680359961, 1.3510086990649872, 0.0)
    viewCenter191 = NXOpen.Point3d(28.371182680359624, -1.3510086990645129, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint191, viewCenter191)
    
    rotMatrix18 = NXOpen.Matrix3x3()
    
    rotMatrix18.Xx = 0.30132677716895906
    rotMatrix18.Xy = -0.94678000767105275
    rotMatrix18.Xz = -0.11318034473956713
    rotMatrix18.Yx = -0.77653607800892144
    rotMatrix18.Yy = -0.17477961184138768
    rotMatrix18.Yz = -0.60534602239965918
    rotMatrix18.Zx = 0.55334789500953452
    rotMatrix18.Zy = 0.27029558701350009
    rotMatrix18.Zz = -0.78787461104514356
    translation18 = NXOpen.Point3d(81.809184428842769, 21.661129953408235, -209.02147090404466)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix18, translation18, 2.663442016194502)
    
    scaleAboutPoint192 = NXOpen.Point3d(-30.894390103613265, 2.2847941234185658, 0.0)
    viewCenter192 = NXOpen.Point3d(30.89439010361291, -2.2847941234180831, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint192, viewCenter192)
    
    scaleAboutPoint193 = NXOpen.Point3d(-24.556569883000662, 1.668893098844938, 0.0)
    viewCenter193 = NXOpen.Point3d(24.556569883000336, -1.6688930988444568, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint193, viewCenter193)
    
    scaleAboutPoint194 = NXOpen.Point3d(-19.518102146488584, 1.1443838392080286, 0.0)
    viewCenter194 = NXOpen.Point3d(19.518102146488253, -1.1443838392075569, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint194, viewCenter194)
    
    scaleAboutPoint195 = NXOpen.Point3d(-24.397627683110692, 1.4304797990099818, 0.0)
    viewCenter195 = NXOpen.Point3d(24.397627683110354, -1.4304797990095006, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint195, viewCenter195)
    
    scaleAboutPoint196 = NXOpen.Point3d(-30.497034603888341, 1.7880997487624088, 0.0)
    viewCenter196 = NXOpen.Point3d(30.497034603887982, -1.7880997487619261, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint196, viewCenter196)
    
    scaleAboutPoint197 = NXOpen.Point3d(-37.997119661196344, 2.2351246859529583, 0.0)
    viewCenter197 = NXOpen.Point3d(37.997119661195967, -2.2351246859524818, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint197, viewCenter197)
    
    scaleAboutPoint198 = NXOpen.Point3d(-47.496399576495378, 2.793905857441132, 0.0)
    viewCenter198 = NXOpen.Point3d(47.496399576495008, -2.7939058574406554, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint198, viewCenter198)
    
    scaleAboutPoint199 = NXOpen.Point3d(-59.370499470619151, 3.10433984160123, 0.0)
    viewCenter199 = NXOpen.Point3d(59.370499470618824, -3.1043398416007504, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint199, viewCenter199)
    
    scaleAboutPoint200 = NXOpen.Point3d(-73.970597788148865, 3.8804248020014747, 0.0)
    viewCenter200 = NXOpen.Point3d(73.970597788148496, -3.8804248020009782, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint200, viewCenter200)
    
    markId44 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "復原上一個約束")
    
    componentConstraint8.FlipAlignment()
    
    componentNetwork9.Solve()
    
    rotMatrix19 = NXOpen.Matrix3x3()
    
    rotMatrix19.Xx = 0.36560052624949219
    rotMatrix19.Xy = -0.92031569357489307
    rotMatrix19.Xz = -0.13912325242695686
    rotMatrix19.Yx = -0.5095015227421853
    rotMatrix19.Yy = -0.072792193455306728
    rotMatrix19.Yz = -0.85738526631576639
    rotMatrix19.Zx = 0.77893802932549328
    rotMatrix19.Zy = 0.38434401352398462
    rotMatrix19.Zz = -0.49551511151405453
    translation19 = NXOpen.Point3d(24.837588198417428, 48.012022096333745, -193.87798663937016)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix19, translation19, 0.87275667986661465)
    
    componentPositioner9.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner9.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId42, None)
    
    theSession.UndoToMark(markId41, None)
    
    theSession.DeleteUndoMark(markId41, None)
    
    theSession.DeleteUndoMark(markId40, None)
    
    # ----------------------------------------------
    #   功能表：編輯(E)->刪除(D)...
    # ----------------------------------------------
    markId45 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Delete")
    
    notifyOnDelete1 = theSession.Preferences.Modeling.NotifyOnDelete
    
    theSession.UpdateManager.ClearErrorList()
    
    markId46 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Delete")
    
    objects14 = [NXOpen.TaggedObject.Null] * 1 
    displayedConstraint1 = workPart.FindObject("ENTITY 160 2 1")
    objects14[0] = displayedConstraint1
    nErrs38 = theSession.UpdateManager.AddObjectsToDeleteList(objects14)
    
    notifyOnDelete2 = theSession.Preferences.Modeling.NotifyOnDelete
    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs39 = theSession.UpdateManager.DoUpdate(id1)
    
    theSession.DeleteUndoMark(markId45, None)
    
    # ----------------------------------------------
    #   功能表：組立件(A)->元件位置(P)->移動元件(E)...
    # ----------------------------------------------
    markId47 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    componentPositioner10 = workPart.ComponentAssembly.Positioner
    
    componentPositioner10.ClearNetwork()
    
    componentPositioner10.PrimaryArrangement = arrangement1
    
    componentPositioner10.BeginMoveComponent()
    
    allowInterpartPositioning10 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression73 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression74 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression75 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression76 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression77 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression78 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression79 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression80 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network10 = componentPositioner10.EstablishNetwork()
    
    componentNetwork10 = network10
    componentNetwork10.MoveObjectsState = True
    
    componentNetwork10.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork10.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    expression81 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression82 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression83 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression84 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression85 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    componentNetwork10.RemoveAllConstraints()
    
    movableObjects1 = []
    componentNetwork10.SetMovingGroup(movableObjects1)
    
    componentNetwork10.Solve()
    
    theSession.SetUndoMarkName(markId47, "移動元件 對話方塊")
    
    componentNetwork10.MoveObjectsState = True
    
    markId48 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Move Component Update")
    
    componentPositioner10.EndMoveComponent()
    
    componentPositioner10.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    theSession.DeleteUndoMarksUpToMark(markId48, None, False)
    
    theSession.UndoToMark(markId47, None)
    
    theSession.DeleteUndoMark(markId47, None)
    
    # ----------------------------------------------
    #   功能表：組立件(A)->元件位置(P)->組立約束(N)...
    # ----------------------------------------------
    markId49 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "通過定位任務建立約束")
    
    markId50 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "起點")
    
    componentPositioner11 = workPart.ComponentAssembly.Positioner
    
    componentPositioner11.ClearNetwork()
    
    componentPositioner11.PrimaryArrangement = arrangement1
    
    componentPositioner11.BeginAssemblyConstraints()
    
    allowInterpartPositioning11 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression86 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression87 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression88 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression89 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression90 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression91 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression92 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression93 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network11 = componentPositioner11.EstablishNetwork()
    
    componentNetwork11 = network11
    componentNetwork11.MoveObjectsState = True
    
    componentNetwork11.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork11.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId50, "組立約束 對話方塊")
    
    componentNetwork11.MoveObjectsState = True
    
    componentNetwork11.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId51 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    line13 = workPart.Lines.CreateFaceAxis(face14, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line13.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    scaleAboutPoint201 = NXOpen.Point3d(201.90335297912685, 49.414784587984769, 0.0)
    viewCenter201 = NXOpen.Point3d(-201.90335297912716, -49.4147845879843, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint201, viewCenter201)
    
    scaleAboutPoint202 = NXOpen.Point3d(160.31004963267591, 39.531827670387869, 0.0)
    viewCenter202 = NXOpen.Point3d(-160.31004963267634, -39.531827670387372, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint202, viewCenter202)
    
    scaleAboutPoint203 = NXOpen.Point3d(127.85999722594062, 31.431440896210272, 0.0)
    viewCenter203 = NXOpen.Point3d(-127.85999722594102, -31.431440896209811, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint203, viewCenter203)
    
    scaleAboutPoint204 = NXOpen.Point3d(102.28799778075252, 24.83471873280816, 0.0)
    viewCenter204 = NXOpen.Point3d(-102.28799778075283, -24.834718732807712, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint204, viewCenter204)
    
    objects15 = [NXOpen.TaggedObject.Null] * 1 
    objects15[0] = line13
    nErrs40 = theSession.UpdateManager.AddObjectsToDeleteList(objects15)
    
    scaleAboutPoint205 = NXOpen.Point3d(42.219021845773348, 3.7252078099214141, 0.0)
    viewCenter205 = NXOpen.Point3d(-42.219021845773668, -3.7252078099209691, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint205, viewCenter205)
    
    scaleAboutPoint206 = NXOpen.Point3d(48.272484536895256, 3.8804248020014565, 0.0)
    viewCenter206 = NXOpen.Point3d(-48.272484536895583, -3.8804248020010199, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint206, viewCenter206)
    
    scaleAboutPoint207 = NXOpen.Point3d(52.57975606711662, 4.8505310025017536, 0.0)
    viewCenter207 = NXOpen.Point3d(-52.579756067116968, -4.8505310025013069, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint207, viewCenter207)
    
    scaleAboutPoint208 = NXOpen.Point3d(59.176478230518732, 7.0332699536274683, 0.0)
    viewCenter208 = NXOpen.Point3d(-59.176478230519066, -7.0332699536270136, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint208, viewCenter208)
    
    scaleAboutPoint209 = NXOpen.Point3d(-79.730603353619401, 6.6694801284398206, 0.0)
    viewCenter209 = NXOpen.Point3d(79.730603353619088, -6.669480128439381, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint209, viewCenter209)
    
    scaleAboutPoint210 = NXOpen.Point3d(-107.62115661800335, 8.3368501605497443, 0.0)
    viewCenter210 = NXOpen.Point3d(107.62115661800297, -8.3368501605492913, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint210, viewCenter210)
    
    scaleAboutPoint211 = NXOpen.Point3d(-189.47386728521698, -17.05264805566927, 0.0)
    viewCenter211 = NXOpen.Point3d(189.47386728521664, 17.052648055669714, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint211, viewCenter211)
    
    scaleAboutPoint212 = NXOpen.Point3d(-152.71593703188495, -15.157909382817127, 0.0)
    viewCenter212 = NXOpen.Point3d(152.71593703188455, 15.15790938281758, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint212, viewCenter212)
    
    scaleAboutPoint213 = NXOpen.Point3d(-122.17274962550795, -13.338960256879046, 0.0)
    viewCenter213 = NXOpen.Point3d(122.17274962550765, 13.338960256879487, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint213, viewCenter213)
    
    scaleAboutPoint214 = NXOpen.Point3d(-97.49567315028132, -10.913694755628281, 0.0)
    viewCenter214 = NXOpen.Point3d(97.495673150280993, 10.913694755628715, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint214, viewCenter214)
    
    scaleAboutPoint215 = NXOpen.Point3d(-77.996538520225087, -8.7309558045025746, 0.0)
    viewCenter215 = NXOpen.Point3d(77.996538520224746, 8.7309558045030045, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint215, viewCenter215)
    
    scaleAboutPoint216 = NXOpen.Point3d(-61.465928863699816, -5.5878117148815729, 0.0)
    viewCenter216 = NXOpen.Point3d(61.465928863699446, 5.5878117148819966, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint216, viewCenter216)
    
    scaleAboutPoint217 = NXOpen.Point3d(-49.172743090959891, -4.4702493719052159, 0.0)
    viewCenter217 = NXOpen.Point3d(49.172743090959528, 4.470249371905628, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint217, viewCenter217)
    
    scaleAboutPoint218 = NXOpen.Point3d(-39.238855597836725, -3.5761994975241387, 0.0)
    viewCenter218 = NXOpen.Point3d(39.238855597836348, 3.5761994975245539, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint218, viewCenter218)
    
    scaleAboutPoint219 = NXOpen.Point3d(-31.391084478269413, -2.8609595980192633, 0.0)
    viewCenter219 = NXOpen.Point3d(31.391084478269036, 2.8609595980196834, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint219, viewCenter219)
    
    scaleAboutPoint220 = NXOpen.Point3d(-22.696946144287999, 0.12715375991218617, 0.0)
    viewCenter220 = NXOpen.Point3d(22.696946144287619, -0.12715375991176334, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint220, viewCenter220)
    
    rotMatrix20 = NXOpen.Matrix3x3()
    
    rotMatrix20.Xx = 0.21395180362315616
    rotMatrix20.Xy = -0.96607974383801287
    rotMatrix20.Xz = -0.14461865119089259
    rotMatrix20.Yx = 0.10006739300955485
    rotMatrix20.Yy = 0.16894354022213628
    rotMatrix20.Yz = -0.98053281284895222
    rotMatrix20.Zx = 0.97170527557622133
    rotMatrix20.Zy = 0.19531515241548802
    rotMatrix20.Zz = 0.13281885654621758
    translation20 = NXOpen.Point3d(91.972169900775256, -13.482813052834516, -190.63389189883182)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix20, translation20, 5.2020351878798863)
    
    markId52 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint9 = componentPositioner11.CreateConstraint(True)
    
    componentConstraint9 = constraint9
    componentConstraint9.ConstraintAlignment = NXOpen.Positioning.Constraint.Alignment.InferAlign
    
    componentConstraint9.ConstraintType = NXOpen.Positioning.Constraint.Type.Touch
    
    constraintReference17 = componentConstraint9.CreateConstraintReference(component5, face10, False, False, False)
    
    helpPoint17 = NXOpen.Point3d(23.338913438290767, -182.58997560334763, -2.7460082682182474)
    constraintReference17.HelpPoint = helpPoint17
    
    constraintReference18 = componentConstraint9.CreateConstraintReference(component1, face13, False, False, False)
    
    helpPoint18 = NXOpen.Point3d(33.338913438299862, 122.31640698610138, 4.2946705886777172)
    constraintReference18.HelpPoint = helpPoint18
    
    constraintReference18.SetFixHint(True)
    
    componentConstraint9.SetAlignmentHint(NXOpen.Positioning.Constraint.Alignment.ContraAlign)
    
    componentNetwork11.Solve()
    
    scaleAboutPoint221 = NXOpen.Point3d(-19.276510002655826, 5.5947654361271715, 0.0)
    viewCenter221 = NXOpen.Point3d(19.27651000265546, -5.5947654361267638, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint221, viewCenter221)
    
    scaleAboutPoint222 = NXOpen.Point3d(-24.09563750331974, 6.9298799152029202, 0.0)
    viewCenter222 = NXOpen.Point3d(24.095637503319359, -6.9298799152025197, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint222, viewCenter222)
    
    scaleAboutPoint223 = NXOpen.Point3d(-30.040075779204642, 8.5034076941136405, 0.0)
    viewCenter223 = NXOpen.Point3d(30.040075779204276, -8.5034076941132266, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint223, viewCenter223)
    
    scaleAboutPoint224 = NXOpen.Point3d(-37.450755849074525, 10.529920742710758, 0.0)
    viewCenter224 = NXOpen.Point3d(37.450755849074149, -10.529920742710342, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint224, viewCenter224)
    
    scaleAboutPoint225 = NXOpen.Point3d(-46.440924030350963, 12.665706553732244, 0.0)
    viewCenter225 = NXOpen.Point3d(46.440924030350622, -12.665706553731832, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint225, viewCenter225)
    
    scaleAboutPoint226 = NXOpen.Point3d(-44.236842742814254, 0.62086796832040081, 0.0)
    viewCenter226 = NXOpen.Point3d(44.236842742813927, -0.62086796831999047, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint226, viewCenter226)
    
    scaleAboutPoint227 = NXOpen.Point3d(-55.102032188417724, 2.1506219706857364e-13, 0.0)
    viewCenter227 = NXOpen.Point3d(55.102032188417397, 2.1506219706857364e-13, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint227, viewCenter227)
    
    scaleAboutPoint228 = NXOpen.Point3d(-68.392487135271949, -1.2126327506251933, 0.0)
    viewCenter228 = NXOpen.Point3d(68.392487135271594, 1.2126327506256069, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint228, viewCenter228)
    
    face16 = component1.FindObject("PROTO#.Features|EXTRUDE(2)|FACE 140 {(25,50,29) EXTRUDE(1)}")
    line14 = workPart.Lines.CreateFaceAxis(face16, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line14.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    rotMatrix21 = NXOpen.Matrix3x3()
    
    rotMatrix21.Xx = 0.24197398479575002
    rotMatrix21.Xy = -0.95668016549889923
    rotMatrix21.Xz = -0.16190012854554697
    rotMatrix21.Yx = -0.80723091775863831
    rotMatrix21.Yy = -0.10590850577798863
    rotMatrix21.Yz = -0.58065620966146314
    rotMatrix21.Zx = 0.53835567805736795
    rotMatrix21.Zy = 0.27119448619924419
    rotMatrix21.Zz = -0.79788891116402638
    translation21 = NXOpen.Point3d(13.006335834283458, -74.452657756621988, -208.35603420794689)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix21, translation21, 0.87275667986661465)
    
    objects16 = [NXOpen.TaggedObject.Null] * 1 
    objects16[0] = line14
    nErrs41 = theSession.UpdateManager.AddObjectsToDeleteList(objects16)
    
    markId53 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs42 = theSession.UpdateManager.DoUpdate(markId51)
    
    componentNetwork11.Solve()
    
    componentPositioner11.ClearNetwork()
    
    nErrs43 = theSession.UpdateManager.AddToDeleteList(componentNetwork11)
    
    componentPositioner11.DeleteNonPersistentConstraints()
    
    nErrs44 = theSession.UpdateManager.DoUpdate(markId51)
    
    theSession.DeleteUndoMark(markId53, None)
    
    theSession.SetUndoMarkName(markId50, "組立約束")
    
    componentPositioner11.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner11.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId51, None)
    
    theSession.DeleteUndoMark(markId52, None)
    
    markId54 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner12 = workPart.ComponentAssembly.Positioner
    
    componentPositioner12.ClearNetwork()
    
    componentPositioner12.PrimaryArrangement = arrangement1
    
    componentPositioner12.BeginAssemblyConstraints()
    
    allowInterpartPositioning12 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression94 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression95 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression96 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression97 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression98 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression99 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression100 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression101 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network12 = componentPositioner12.EstablishNetwork()
    
    componentNetwork12 = network12
    componentNetwork12.MoveObjectsState = True
    
    componentNetwork12.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork12.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId54, "組立約束 對話方塊")
    
    componentNetwork12.MoveObjectsState = True
    
    componentNetwork12.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId55 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    rotMatrix22 = NXOpen.Matrix3x3()
    
    rotMatrix22.Xx = 0.24197398479575002
    rotMatrix22.Xy = -0.95668016549889923
    rotMatrix22.Xz = -0.16190012854554697
    rotMatrix22.Yx = -0.70346753235084147
    rotMatrix22.Yy = -0.058053345248338509
    rotMatrix22.Yz = -0.70835248290218578
    rotMatrix22.Zx = 0.66826792651621325
    rotMatrix22.Zy = 0.28529435684302534
    rotMatrix22.Zz = -0.68704083455296938
    translation22 = NXOpen.Point3d(13.006335834283458, -64.95008029733782, -200.39213163340949)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix22, translation22, 0.87275667986661465)
    
    line15 = workPart.Lines.CreateFaceAxis(face14, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    line15.SetVisibility(NXOpen.SmartObject.VisibilityOption.Visible)
    
    objects17 = [NXOpen.TaggedObject.Null] * 1 
    objects17[0] = line15
    nErrs45 = theSession.UpdateManager.AddObjectsToDeleteList(objects17)
    
    scaleAboutPoint229 = NXOpen.Point3d(202.5096693544393, -72.757965037522993, 0.0)
    viewCenter229 = NXOpen.Point3d(-202.50966935443961, 72.757965037523405, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint229, viewCenter229)
    
    scaleAboutPoint230 = NXOpen.Point3d(161.52268238330129, -57.721318929768188, 0.0)
    viewCenter230 = NXOpen.Point3d(-161.52268238330163, 57.7213189297686, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint230, viewCenter230)
    
    scaleAboutPoint231 = NXOpen.Point3d(128.44206094624073, -45.594991423514315, 0.0)
    viewCenter231 = NXOpen.Point3d(-128.44206094624104, 45.594991423514742, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint231, viewCenter231)
    
    line16 = workPart.Lines.CreateFaceAxis(face14, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    objects18 = [NXOpen.TaggedObject.Null] * 1 
    objects18[0] = line16
    nErrs46 = theSession.UpdateManager.AddObjectsToDeleteList(objects18)
    
    scaleAboutPoint232 = NXOpen.Point3d(9.9338874931229988, -19.246907017925928, 0.0)
    viewCenter232 = NXOpen.Point3d(-9.933887493123315, 19.24690701792635, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint232, viewCenter232)
    
    scaleAboutPoint233 = NXOpen.Point3d(-6.4027009233022047, -20.178208970406221, 0.0)
    viewCenter233 = NXOpen.Point3d(6.4027009233018735, 20.178208970406654, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint233, viewCenter233)
    
    scaleAboutPoint234 = NXOpen.Point3d(-24.737708112758078, -22.55496916163197, 0.0)
    viewCenter234 = NXOpen.Point3d(24.737708112757666, 22.554969161632386, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint234, viewCenter234)
    
    scaleAboutPoint235 = NXOpen.Point3d(-45.776886336108483, -25.768445950789253, 0.0)
    viewCenter235 = NXOpen.Point3d(45.776886336108149, 25.768445950789694, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint235, viewCenter235)
    
    scaleAboutPoint236 = NXOpen.Point3d(-92.463247235185804, -29.936871031063998, 0.0)
    viewCenter236 = NXOpen.Point3d(92.463247235185491, 29.936871031064449, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint236, viewCenter236)
    
    scaleAboutPoint237 = NXOpen.Point3d(-182.84228193023424, -55.421106180925591, 0.0)
    viewCenter237 = NXOpen.Point3d(182.84228193023375, 55.421106180926081, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint237, viewCenter237)
    
    scaleAboutPoint238 = NXOpen.Point3d(-229.73706408332527, -71.052700231955995, 0.0)
    viewCenter238 = NXOpen.Point3d(229.73706408332484, 71.052700231956393, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint238, viewCenter238)
    
    scaleAboutPoint239 = NXOpen.Point3d(-355.26350115978113, -159.12844322781839, 0.0)
    viewCenter239 = NXOpen.Point3d(355.26350115978067, 159.12844322781876, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint239, viewCenter239)
    
    scaleAboutPoint240 = NXOpen.Point3d(-284.8029067630913, -128.48696625278728, 0.0)
    viewCenter240 = NXOpen.Point3d(284.80290676309085, 128.48696625278768, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint240, viewCenter240)
    
    scaleAboutPoint241 = NXOpen.Point3d(-227.84232541047311, -102.78957300222977, 0.0)
    viewCenter241 = NXOpen.Point3d(227.84232541047263, 102.78957300223017, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint241, viewCenter241)
    
    scaleAboutPoint242 = NXOpen.Point3d(-182.27386032837848, -82.610606136354221, 0.0)
    viewCenter242 = NXOpen.Point3d(182.27386032837808, 82.610606136354605, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint242, viewCenter242)
    
    scaleAboutPoint243 = NXOpen.Point3d(-145.81908826270279, -66.088484909083363, 0.0)
    viewCenter243 = NXOpen.Point3d(145.81908826270245, 66.088484909083718, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint243, viewCenter243)
    
    rotMatrix23 = NXOpen.Matrix3x3()
    
    rotMatrix23.Xx = 0.21935407131694626
    rotMatrix23.Xy = -0.96304201443658233
    rotMatrix23.Xz = -0.15631337059448652
    rotMatrix23.Yx = -0.32611400631580012
    rotMatrix23.Yy = 0.078627244334726523
    rotMatrix23.Yz = -0.94205488764348633
    rotMatrix23.Zx = 0.91952892628852811
    rotMatrix23.Zy = 0.25761955453392177
    rotMatrix23.Zz = -0.29681428341709842
    translation23 = NXOpen.Point3d(8.9652104387949674, 48.297024220090982, -188.21812929177651)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix23, translation23, 1.0909458498332685)
    
    scaleAboutPoint244 = NXOpen.Point3d(-107.92431480565946, 19.159597459881297, 0.0)
    viewCenter244 = NXOpen.Point3d(107.92431480565917, -19.159597459880885, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint244, viewCenter244)
    
    scaleAboutPoint245 = NXOpen.Point3d(-85.563366884127404, 16.297784168405403, 0.0)
    viewCenter245 = NXOpen.Point3d(85.563366884127063, -16.297784168404974, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint245, viewCenter245)
    
    scaleAboutPoint246 = NXOpen.Point3d(-67.053740578581511, 14.745614247604909, 0.0)
    viewCenter246 = NXOpen.Point3d(67.053740578581198, -14.745614247604486, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint246, viewCenter246)
    
    rotMatrix24 = NXOpen.Matrix3x3()
    
    rotMatrix24.Xx = 0.19679924532407167
    rotMatrix24.Xy = -0.96685501375171057
    rotMatrix24.Xz = -0.16266972497381074
    rotMatrix24.Yx = -0.27531632798223948
    rotMatrix24.Yy = 0.10474180660772622
    rotMatrix24.Yz = -0.9556307202549138
    rotMatrix24.Zx = 0.9409946740477606
    rotMatrix24.Zy = 0.23285303590833642
    rotMatrix24.Zz = -0.24557786358305814
    translation24 = NXOpen.Point3d(59.52541699425835, 42.490966723855607, -187.95660394994064)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix24, translation24, 2.1307536129556022)
    
    line17 = workPart.Lines.CreateFaceAxis(face15, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId56 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Create Constraint")
    
    constraint10 = componentPositioner12.CreateConstraint(True)
    
    componentConstraint10 = constraint10
    componentConstraint10.ConstraintType = NXOpen.Positioning.Constraint.Type.Concentric
    
    edge7 = component5.FindObject("PROTO#.Features|EXTRUDE(1)|EDGE * 130 * 140 {(40,-2.5000000000001,4.3301270189223)(40,5.0000000000001,-0)(40,-2.5000000000001,-4.3301270189223) EXTRUDE(1)}")
    constraintReference19 = componentConstraint10.CreateConstraintReference(component5, edge7, False, False, False)
    
    helpPoint19 = NXOpen.Point3d(33.338913438327154, -178.81038823842295, -3.9192159647862432)
    constraintReference19.HelpPoint = helpPoint19
    
    edge8 = component1.FindObject("PROTO#.Features|EXTRUDE(3)|EDGE * 130 * 160 {(30,87.5,1.6698729810778)(30,95,6)(30,87.5,10.3301270189222) EXTRUDE(1)}")
    constraintReference20 = componentConstraint10.CreateConstraintReference(component1, edge8, False, False, False)
    
    helpPoint20 = NXOpen.Point3d(33.33891343832714, 121.74674071400429, 9.9549552350663912)
    constraintReference20.HelpPoint = helpPoint20
    
    constraintReference20.SetFixHint(True)
    
    objects19 = [NXOpen.TaggedObject.Null] * 1 
    objects19[0] = line17
    nErrs47 = theSession.UpdateManager.AddObjectsToDeleteList(objects19)
    
    componentNetwork12.Solve()
    
    markId57 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "組立約束")
    
    nErrs48 = theSession.UpdateManager.DoUpdate(markId55)
    
    componentNetwork12.Solve()
    
    componentPositioner12.ClearNetwork()
    
    nErrs49 = theSession.UpdateManager.AddToDeleteList(componentNetwork12)
    
    componentPositioner12.DeleteNonPersistentConstraints()
    
    nErrs50 = theSession.UpdateManager.DoUpdate(markId55)
    
    theSession.DeleteUndoMark(markId57, None)
    
    theSession.SetUndoMarkName(markId54, "組立約束")
    
    componentPositioner12.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner12.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId55, None)
    
    theSession.DeleteUndoMark(markId56, None)
    
    markId58 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    componentPositioner13 = workPart.ComponentAssembly.Positioner
    
    componentPositioner13.ClearNetwork()
    
    componentPositioner13.PrimaryArrangement = arrangement1
    
    componentPositioner13.BeginAssemblyConstraints()
    
    allowInterpartPositioning13 = theSession.Preferences.Assemblies.InterpartPositioning
    
    expression102 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", NXOpen.Unit.Null)
    
    expression103 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression104 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit1)
    
    expression105 = workPart.Expressions.CreateSystemExpressionWithUnits("0.0", unit2)
    
    expression106 = workPart.Expressions.CreateSystemExpressionWithUnits("1", NXOpen.Unit.Null)
    
    expression107 = workPart.Expressions.CreateSystemExpressionWithUnits("1.0", unit1)
    
    expression108 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression109 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit2)
    
    network13 = componentPositioner13.EstablishNetwork()
    
    componentNetwork13 = network13
    componentNetwork13.MoveObjectsState = True
    
    componentNetwork13.DisplayComponent = NXOpen.Assemblies.Component.Null
    
    componentNetwork13.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    theSession.SetUndoMarkName(markId58, "組立約束 對話方塊")
    
    componentNetwork13.MoveObjectsState = True
    
    componentNetwork13.NetworkArrangementsMode = NXOpen.Positioning.ComponentNetwork.ArrangementsMode.Existing
    
    markId59 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Assembly Constraints Update")
    
    # ----------------------------------------------
    #   對話開始 組立約束
    # ----------------------------------------------
    scaleAboutPoint247 = NXOpen.Point3d(-66.06035182926918, 12.789880147396282, 0.0)
    viewCenter247 = NXOpen.Point3d(66.060351829268882, -12.789880147395859, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint247, viewCenter247)
    
    scaleAboutPoint248 = NXOpen.Point3d(-82.575439786586443, 15.987350184245297, 0.0)
    viewCenter248 = NXOpen.Point3d(82.575439786586116, -15.98735018424486, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint248, viewCenter248)
    
    scaleAboutPoint249 = NXOpen.Point3d(-103.21929973323297, 19.984187730306569, 0.0)
    viewCenter249 = NXOpen.Point3d(103.2192997332327, -19.984187730306139, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint249, viewCenter249)
    
    rotMatrix25 = NXOpen.Matrix3x3()
    
    rotMatrix25.Xx = 0.69924287625636417
    rotMatrix25.Xy = -0.21999554206478389
    rotMatrix25.Xz = -0.6801921504077707
    rotMatrix25.Yx = -0.60985243155549307
    rotMatrix25.Yy = -0.68002850001848103
    rotMatrix25.Yz = -0.4069904800956225
    rotMatrix25.Zx = -0.37301395648229857
    rotMatrix25.Zy = 0.69940203076216023
    rotMatrix25.Zz = -0.60966990054880077
    translation25 = NXOpen.Point3d(-10.093683364731731, 74.571053340693638, -300.65983109048994)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix25, translation25, 1.0909458498332685)
    
    rotMatrix26 = NXOpen.Matrix3x3()
    
    rotMatrix26.Xx = 0.41734403374438866
    rotMatrix26.Xy = 0.16099788972091139
    rotMatrix26.Xz = -0.89437332082490684
    rotMatrix26.Yx = -0.60985243155549307
    rotMatrix26.Yy = -0.68002850001848103
    rotMatrix26.Yz = -0.4069904800956225
    rotMatrix26.Zx = -0.67372395624900638
    rotMatrix26.Zy = 0.7152907930821033
    rotMatrix26.Zz = -0.18562088273725741
    translation26 = NXOpen.Point3d(-50.009328087722793, 74.571053340693638, -325.99396347391189)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix26, translation26, 1.0909458498332685)
    
    line18 = workPart.Lines.CreateFaceAxis(face9, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    componentPositioner13.PrimaryArrangement = NXOpen.Assemblies.Arrangement.Null
    
    componentPositioner13.EndAssemblyConstraints()
    
    theSession.DeleteUndoMark(markId59, None)
    
    objects20 = [NXOpen.TaggedObject.Null] * 1 
    objects20[0] = line18
    nErrs51 = theSession.UpdateManager.AddObjectsToDeleteList(objects20)
    
    theSession.UndoToMark(markId58, None)
    
    theSession.DeleteUndoMark(markId58, None)
    
    theSession.DeleteUndoMark(markId49, None)
    
    rotMatrix27 = NXOpen.Matrix3x3()
    
    rotMatrix27.Xx = 0.76861946112039725
    rotMatrix27.Xy = -0.48381483874388842
    rotMatrix27.Xz = -0.41850606423110842
    rotMatrix27.Yx = -0.54234068917935119
    rotMatrix27.Yy = -0.83977998544375576
    rotMatrix27.Yz = -0.025222071852829504
    rotMatrix27.Zx = -0.33925020390186034
    rotMatrix27.Zy = 0.24635904257669822
    rotMatrix27.Zz = -0.9078637129510313
    translation27 = NXOpen.Point3d(7.9907389492071275, 84.995537151306053, -267.84269004396765)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix27, translation27, 1.0909458498332691)
    
    scaleAboutPoint250 = NXOpen.Point3d(-11.398747855878767, 16.734331958630513, 0.0)
    viewCenter250 = NXOpen.Point3d(11.398747855878456, -16.734331958630122, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint250, viewCenter250)
    
    scaleAboutPoint251 = NXOpen.Point3d(-14.248434819848459, 20.917914948288118, 0.0)
    viewCenter251 = NXOpen.Point3d(14.248434819848123, -20.917914948287706, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint251, viewCenter251)
    
    scaleAboutPoint252 = NXOpen.Point3d(-17.810543524810573, 26.147393685360047, 0.0)
    viewCenter252 = NXOpen.Point3d(17.810543524810186, -26.147393685359724, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint252, viewCenter252)
    
    scaleAboutPoint253 = NXOpen.Point3d(-22.263179406013137, 32.684242106700026, 0.0)
    viewCenter253 = NXOpen.Point3d(22.263179406012814, -32.684242106699699, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(0.80000000000000004, scaleAboutPoint253, viewCenter253)
    
    # ----------------------------------------------
    #   功能表：工具(T)->動作記錄(J)->停止錄製(S)
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()